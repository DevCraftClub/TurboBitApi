from datetime import datetime
from typing import Union

from turbobit import str_to_datetime, toint
from turbobit.responses import Response


class FileInfoResponse(Response):
	"""
	Response for file information

	**Example response**:

	```json

	{
	    "id":"nn9ll2t512ot",
	    "name":"Archive.zip",
	    "size":"1299992",
	    "state":"active",
	    "folder_id":"0",
	    "created_date":"2018-09-17 23:58:00",
	    "deleted_date":"2018-10-27 23:58:00"
	}

	```
	"""

	id: str
	name: str
	size: Union[int, str]
	state: str
	folder_id: Union[int, str]
	created_at: Union[datetime, str]
	deleted_date: Union[datetime, str]

	def get_size(self) -> int:
		"""
		The get_size function returns the size of the file in bytes.
		It is a wrapper for toint, which converts a string into an integer.

		**Return**: The size of the object in bytes
		"""
		return toint(self.size)

	def get_folder_id(self) -> int:
		"""
		The get_folder_id function returns the folder_id as an integer.

		**Return**: The folder_id as an integer.
		"""
		return toint(self.folder_id)

	def get_created_at(self) -> datetime:
		"""
		The get_created_at function is a helper function that returns the created_at attribute of an instance of the datetime class. If the created_at attribute is not a datetime object, it will be converted to one before being returned.

		**Return**: The created_at as `datetime.datetime` object
		"""
		if isinstance(self.created_at, str):
			return str_to_datetime(self.created_at)
		return self.created_at

	def get_deleted_date(self) -> datetime:
		"""
		The get_deleted_date function is a helper function that returns the deleted_date attribute of an instance of the datetime class. If the deleted_date attribute is not a datetime object, it will be converted to one before being returned.

		**Return**: The deleted date of the object as `datetime.datetime`
		"""

		if isinstance(self.deleted_date, str):
			return str_to_datetime(self.deleted_date)
		return self.deleted_date
