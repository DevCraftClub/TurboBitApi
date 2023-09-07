from typing import Optional

from turbobit.classes import Connect
from turbobit.responses import Response
from turbobit.responses.CheckRemoteUploadResponse import CheckRemoteUploadResponse
from turbobit.responses.RemoteUploadResponse import RemoteUploadResponse


class Remote(Connect):
	urls: list[str] = []
	service: str = 'http'
	login: Optional[str] = None
	password: Optional[str] = None

	def __init__(self, urls: list, service: Optional[str] = None, login: Optional[str] = None,
	             password: Optional[str] = None):

		"""
		The __init__ function for remote upload

		**Args**:

		- `urls`: list: Set the urls attribute of the class

		- `service`: str: Set the service name (Optional)

		- `login`: str: Set the login for the service. Required for non-http services (Optional)

		- `password`: str: Set the password of the service. Required for non-http services (Optional)

		"""
		super().__init__()
		self.urls = urls
		self.set_service(service or self.service, login, password)

	def set_service(self, service: str, login: Optional[str] = None, password: Optional[str] = None):
		"""
		The set_service function is used to set the service that will be used for remote upload from a service.

		Auth data is **required** when non-http service is used

		**Args**:

		- `service`: str: Set the service that will be used to download the file. By default: `http`

		- `login`: str: Set the login parameter (Optional)

		- `password`: str: Set the password of the account (Optional)

		**Available services**:

		- http (by default)

		- ftp

		- 1fichier

		- depositfiles

		- fileal

		- fileboom

		- filejoker

		- hitfile

		- keep2share

		- nitroflare

		- rapidgator

		- turbobit

		- uploadable

		- uploaded

		**Return**: Only when error occurs, function returns `turbobit.responses.Response.error_response`
		"""
		available_services = ['http', 'ftp', '1fichier', 'depositfiles', 'fileal', 'fileboom', 'filejoker', 'hitfile',
		                      'keep2share', 'nitroflare', 'rapidgator', 'turbobit', 'uploadable', 'uploaded']
		none_login_service = ['http']
		if service in available_services:
			if service not in none_login_service:
				if login is None or password is None:
					return Response.error_response("Login and password are required but are not provided!",
					                               self.__class__, 'set_service', login=login, password=password,
					                               service=service)
				else:
					self.login = login
					self.password = password
			self.service = service
		else:
			return Response.error_response("Given service is not provided by API", self.__class__,
			                               'set_service', login=login, password=password, service=service)

	def upload(self) -> RemoteUploadResponse:
		"""
		The upload function is used to upload files from remote servers.

		**Link**: [#remote](https://turbobit.net/api#remote)

		**Return**: `turbobit.responses.RemoteUploadResponse.RemoteUploadResponse`
		"""
		return self.send_request('https://turbobit.net/v001/remote_upload', 'POST', headers={
			'X-API-KEY': self.api_key
		}, data={
			'url'     : '\n'.join(self.urls),
			'service' : self.service,
			'login'   : self.login,
			'password': self.password
		})

	def check_upload(self, download_id: str) -> CheckRemoteUploadResponse:
		"""
		The check_upload function is used to check the status of a remote upload.

		**Args**:

		- `download_id`: str: File ID of the remote uploaded file you want to check

		**Return**: `turbobit.responses.CheckRemoteUploadResponse.CheckRemoteUploadResponse`
		"""
		status = self.send_request(f'https://turbobit.net/v001/remote_upload/status/{download_id}', headers={
			'X-API-KEY': self.api_key
		})

		if status.error is None:
			return status
		return status.error_response(status.error, self.__class__, 'check_upload', status_data=status)
