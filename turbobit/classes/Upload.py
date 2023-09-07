import traceback
from typing import Optional

import fsutil

from turbobit.classes import Connect
from turbobit.responses.UploadFileResponse import UploadFileResponse
from turbobit.responses.UploadUrlResponse import UploadUrlResponse


class UploadFile(Connect):
	file_path: Optional[str] = None

	def __init__(self, file_path: str):
		"""
		The __init__ method sets the file path or keeps as `None` if file is not found on server

		**Args**:

		- `file_path`: str: The absolute path to the file to upload on server
		"""
		super().__init__()
		if fsutil.is_file(file_path):
			self.file_path = file_path

	def _get_upload_data(self) -> Optional[UploadUrlResponse]:
		"""
		The _get_upload_data function is used to get the upload data from the server.

		**Return**:

		- `turbobit.responses.UploadUrlResponse.UploadUrlResponse` when successful

		- None when failure
		"""
		if self.api_key is not None:
			return self.send_request('https://turbobit.net/v001/upload/http/server', type_request='POST', headers={
				'X-API-KEY': self.api_key
			})
		else:
			return UploadUrlResponse.error_response("No API key", self.__class__, "_get_upload_data", api_key=self.api_key)

	def upload(self, folder_id: int = 0) -> Optional[UploadFileResponse]:
		"""
		The upload function is used to upload a file to the TurboBit cloud.
		The function takes in an optional folder_id parameter, which defaults to 2423678 (the root directory).
		It then gets the upload data from _get_upload_data(), and if it exists, sends a POST request with that data.


		**Link**: [#http-upload](https://turbobit.net/api#http-upload)

		**Args**:

		- `folder_id`: int: Specify the folder to upload the file to

		**Return**:

		- `turbobit.responses.UploadFileResponse.UploadFileResponse` when the upload is successful

		- `None` when upload failed
		"""
		data = self._get_upload_data()
		if self.file_path is not None:
			if data is not None:
				data: UploadUrlResponse
				try:
					return self.send_request(data["url"], 'POST', data={
						"apptype"    : data["params"]["apptype"],
						"upload_info": data["params"]["upload_info"],
						"folder_id"  : folder_id
					}, files={
						"Filedata"   : open(self.file_path, 'rb')
					})
				except Exception as e:
					traceback.print_exc()
					return UploadFileResponse.error_response('Couldn\'t be uploaded', self.__class__, 'upload',
					                                         file_path=self.file_path,
					                                         file_exists=fsutil.is_file(self.file_path) or False,
					                                         upload_data=data,
					                                         exception=e)
		else:
			return UploadFileResponse.error_response('No file has been found', self.__class__, 'upload', file_path=self.file_path, file_exists=fsutil.is_file(self.file_path) or False, upload_data=data)
