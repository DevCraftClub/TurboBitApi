from typing import Optional, Union

from turbobit.responses import Response


class CheckRemoteUploadResponse(Response):
	"""
	Response for checking remote upload

	**Example responses**:

	```json

	{
	    "result": true,

	    "state": "created",
	    "progress": "0",

	    "state": "queue",
	    "progress": "0",

	    "state": "running",
	    "progress": "50",

	    "state": "finished",
	    "progress": "100",
	    "file_id": "dyeswq5sy7vt",

	    "state": "error",
	    "error": "Error message"
	}

	```

	"""
	result: bool
	state: str
	error: Optional[str] = None
	progress: Optional[Union[int, str]] = None
	file_id: Optional[str] = None
