from turbobit.responses import Response


class UploadUrlResponseParams:
	"""
	Object for `turbobit.responses.UploadUrlResponse.UploadUrlResponse`
	"""
	apptype: str
	upload_info: str


class UploadUrlResponse(Response):
	"""
	Response for upload data to upload a file to server

	**Example response**:

	```json

	{
	    "url": "http://s209.turbobit.net/uploadfile",
	    "params": {
	            "apptype": "fd1",
	            "upload_info": "F+ZuaV6EN1a4cdftUSIX4ZwMCswN9jB58d0/"
	    },
	    "result": true
	}

	```
	"""
	url: str
	params: UploadUrlResponseParams
	result: bool = False
