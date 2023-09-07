from datetime import datetime
from typing import Optional, Union

from turbobit import str_to_datetime, toint
from turbobit.responses import Response


class Folder:
	"""
	Folder object for Response
	"""
	id: int
	name: str
	files_count: Union[str, int]
	parent_id: Union[str, int]
	created_date: Union[str, datetime]

	def get_files_count(self) -> int:
		"""
		The get_files_count function returns the files_count as an integer.


		**Return**: The files_count attribute as an integer
		"""
		return toint(self.files_count)

	def get_parent_id(self) -> int:
		"""
		The get_parent_id function returns the parent_id as an integer.

		**Return**: The parent_id attribute as an integer
		"""
		return toint(self.files_count)

	def get_created_date(self) -> datetime:
		"""
		The get_created_at function is a helper function that returns the created_date attribute of an instance of the datetime class. If the created_date attribute is not a datetime object, it will be converted to one before being returned.

		**Return**: The created_date as `datetime`
		"""
		if isinstance(self.created_date, str):
			return str_to_datetime(self.created_date)
		return self.created_date


class FolderListResponse(Response):
	"""
	Response for a list of folders

	**Example response**:

	```json

	{
	    "folders": [
	        {
	            "id": 1258713,
	            "name": "Video",
	            "files_count": "44",
	            "parent_id": null,
	            "created_date": "2018-01-01T12:34:42+03:00"
	        },
	        {
	            "id": 1267138,
	            "name": "Clips",
	            "files_count": "20",
	            "parent_id": "1258713",
	            "created_date": "2018-01-03T11:21:32+05:00"
	        }
	    ],
	    "result": true
	}

	```
	"""
	folders: list[Optional[Folder]]
	result: bool
