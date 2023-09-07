import os
import traceback
from pathlib import Path
from typing import Optional, Union

import requests
from dotenv import load_dotenv

from turbobit import ENV_FILE
from turbobit.responses.CheckRemoteUploadResponse import CheckRemoteUploadResponse
from turbobit.responses.FileCopyResponse import FileCopyExtendedResponse, FileCopyResponse
from turbobit.responses.FileInfoResponse import FileInfoResponse
from turbobit.responses.FileSearchResponse import FileSearchResponse
from turbobit.responses.FolderListResponse import FolderListResponse
from turbobit.responses.RemoteUploadResponse import RemoteUploadResponse
from turbobit.responses.UploadFileResponse import UploadFileResponse
from turbobit.responses.UploadUrlResponse import UploadUrlResponse


class Connect:
	api_key: Optional[str] = None

	def __init__(self, api_key: Optional[str] = None):
		"""
		The __init__ function is called when the class is instantiated. It automatically receives the TURBOBIT_API variable from environment.

		Or put in every class the API key on init
		"""
		load_dotenv(dotenv_path=Path(ENV_FILE))
		self.api_key = api_key or os.environ.get('TURBOBIT_API')

	def send_request(self, url: str, type_request: str = 'GET', data: Optional[dict] = None, json_data: Optional[dict] = None,
	                 parameters: Optional[dict] = None, files: Optional[dict] = None, headers: Optional[dict] = None) ->\
	Optional[Union[dict, UploadUrlResponse, UploadFileResponse, FileInfoResponse, FileSearchResponse, FileCopyResponse, FileCopyExtendedResponse, FolderListResponse, RemoteUploadResponse, CheckRemoteUploadResponse]]:
		"""
		The send_request function is used to send a request to the server.

		**Args**:

		- `url`: str: Specify the url that we want to send our request to
		- `type_request`: str: Specify the type of request to be sent (get or post). By default: `GET`
		- `data`: dict: Send data to the server (Optional)
		- `json_data`: dict: Send data to the server (Optional)
		- `parameters`: dict: Pass in a dictionary of parameters to the request (Optional)
		- `files`: dict: Upload a file to the server (Optional)
		- `headers`: dict: Pass the authorization token to the api (Optional)

		**Return**:

		- dict
		- `turbobit.responses.CheckRemoteUploadResponse.CheckRemoteUploadResponse`
		- `turbobit.responses.FileCopyResponse.FileCopyResponse`
		- `turbobit.responses.FileCopyResponse.FileCopyExtendedResponse`
		- `turbobit.responses.FileInfoResponse.FileInfoResponse`
		- `turbobit.responses.FileSearchResponse.FileSearchResponse`
		- `turbobit.responses.FolderListResponse.FolderListResponse`
		- `turbobit.responses.RemoteUploadResponse.RemoteUploadResponse`
		- `turbobit.responses.RemoteUploadResponse.RemoteUploadResponse`
		- `turbobit.responses.UploadFileResponse.UploadFileResponse`
		- `turbobit.responses.UploadUrlResponse.UploadUrlResponse`

		 """
		s = requests.Session()

		if headers is not None:
			headers = headers | {
				"Accept"      : "application/json",
				"Content-Type": "application/json"
			}

		response = None
		try:
			response = s.request(type_request, url, parameters, data, headers, json=json_data, files=files)


		except:
			traceback.print_exc()

		try:
			return response.json()
		except:
			return response
