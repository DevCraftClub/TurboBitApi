from turbobit.responses import Response


class UploadFileResponse(Response):
	"""
	Response for file upload

	**Example response**:

	```json

	{
	     "result":true,
	     "id":"1i555e01nb3",
	     "cid":"6dcUDq1",
	     "message":"Everything is ok"
	}

	```
	"""
	result: bool
	id: str
	cid: str
	message: str
