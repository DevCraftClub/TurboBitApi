from typing import Optional

from turbobit.responses import Response


class RemoteUploadFileMessage:
	"""
	Remote Upload File object for response
	"""
	msg: str
	url: str
	url_download_id: str
	result: bool


class RemoteUploadResponse(Response):
	"""
	Response for remote file upload

	**Example response**:

	```json

	{
	    "message": [
	        {
	            "msg": "File has been added to the upload queue.",
	            "url": "http://domain.com/file_1.zip",
	            "url_download_id": "458AB57FCA8A26B51CEE3B428527832A",
	            "success": true
	        }
	    ],
	    "result": true
	}

	```
	"""
	message: list[Optional[RemoteUploadFileMessage]]
	result: bool
