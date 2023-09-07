from typing import Optional

from turbobit.responses import Response
from turbobit.responses.FileInfoResponse import FileInfoResponse


class FileSearchResponse(Response):
	"""
	Response for file search

	**Example response**:

	```json

	{
	    "results": [
	        {
	         "id":"nn9ll2t5j2ot",
	         "name":"Archive.zip",
	         "size":"1299992",
	         "state":"active",
	         "folder_id":"0",
	         "created_date":"2018-09-17 23:11:00",
	         "deleted_date":"2018-10-27 23:11:00"
	        },
	        {
	         "id":"hhfnn222jdls",
	         "name":"Archive2.zip",
	         "size":"1291192",
	         "state":"active",
	         "folder_id":"0",
	         "created_date":"2018-09-17 23:58:00",
	         "deleted_date":"2018-10-27 23:58:00"
	        },
	    ],
	    "page": 1,
	    "totalPages": 10
	}

	```
	"""
	results: list[Optional[FileInfoResponse]]
	page: int
	totalPages: int
