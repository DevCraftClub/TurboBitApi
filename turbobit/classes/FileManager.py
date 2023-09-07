from typing import Optional

from turbobit.classes import Connect
from turbobit.responses.FileCopyResponse import FileCopyExtendedResponse, FileCopyResponse
from turbobit.responses.FileInfoResponse import FileInfoResponse
from turbobit.responses.FileSearchResponse import FileSearchResponse
from turbobit.responses.FolderListResponse import FolderListResponse


class FileManager(Connect):

	def __init__(self):
		super().__init__()

	def get_file_info(self, file_id: str) -> FileInfoResponse:
		""" 
		The get_file_info function is used to get information about a file.


		**Link**: [#file-info](https://turbobit.net/api#file-info)

		**Args**:

		- `file_id`: str: file ID

		**Return**: `turbobit.responses.FileInfoResponse.FileInfoResponse`
		"""
		return self.send_request(f'https://turbobit.net/v001/files/{file_id}', headers={
			'X-API-KEY': self.api_key
		})

	def search_file(self, name: str, page: int = 1) -> FileSearchResponse:
		""" 
		The search_file function searches for a file on the TurboBit website in profile.

		**Link**: [#file-search](https://turbobit.net/api#file-search)

		**Args**:

		- `name`: str: Search for a file by name
		- `page`: int: Specify the page number of the search results. By default: `1`

		**Return**: `turbobit.responses.FileSearchResponse.FileSearchResponse`
		"""
		return self.send_request(f'https://turbobit.net/v001/files/search?name={name}&page={page}', headers={
			'X-API-KEY': self.api_key
		}, data={'name': name, 'page': page})

	def copy(self, file_id: str) -> FileCopyResponse:
		"""
		The copy function allows you to copy a file by file ID to your files.

		**Link**: [#copy](https://turbobit.net/api#copy)

		**Args**:

		- `file_id`: str: Specify the file ID of the file you want to copy

		**Return**: `turbobit.responses.FileCopyResponse.FileCopyResponse`
		"""
		return self.send_request(f'https://turbobit.net/v001/files/{file_id}/copy', headers={
			'X-API-KEY': self.api_key
		})

	def copy_extended(self, file_id: str, folder_id: Optional[int] = None) -> FileCopyExtendedResponse:
		"""
		The copy_extended function is the extended version of `turbobit.classes.FileManager.copy`. It allows you to copy a file in to a specific folder

		**Link**: [#copyPost](https://turbobit.net/api#copyPost)

		**Args**:

		- `file_id`: str: Specify the file ID to be copied

		- `folder_id`: int: Specify the folder ID to copy the file to (Optional)

		**Return**: `turbobit.responses.FileCopyExtendedResponse.FileCopyExtendedResponse`
		"""
		return self.send_request('https://turbobit.net/v001/files/copy', headers={
			'X-API-KEY': self.api_key
		}, data={'folder_id': folder_id, 'file_id': file_id})

	def get_folder_list(self) -> FolderListResponse:
		""" 
		The get_folder_list function returns a list of all folders in the account.

		**Link**: [#folders-index](https://turbobit.net/api#folders-index)

		**Return**: A list of folders in the account with `turbobit.responses.FolderListResponse.FolderListResponse`
		"""
		return self.send_request('https://turbobit.net/v001/folders/index', headers={
			'X-API-KEY': self.api_key
		})
