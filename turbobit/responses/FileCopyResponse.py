from datetime import datetime
from typing import Union

from turbobit import str_to_datetime, toint
from turbobit.responses import Response


class FileCopyResponse(Response):
	"""
	Response for file copy

	**Example response**:

	```json

	{
		"id": "hh17hhdllajf",
		"result": true
	}
	```
	"""
	id: str
	result: bool


class FileCopyExtendedResponse(FileCopyResponse):
	"""
	Response for file copy (extended version)

	**Example response**:

	```json

	{
		"id": "hh17hhdllajf",
		"name": "File name",
		"size": "1024",
		"folder_id": "18954",
		"created_date": "2021-08-29T16:03:15+03:00",
		"result": true
	}
	```
	"""

	name: str
	size: Union[str, int]
	folder_id: Union[str, int]
	created_date: Union[datetime, str]

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

		**Return**: The folder_id attribute as an integer
		"""
		return toint(self.folder_id)

	def get_created_at(self) -> datetime:
		"""
		The get_created_at function is a helper function that returns the created_date attribute of an instance of the datetime class. If the created_date attribute is not a datetime object, it will be converted to one before being returned.


		**Return**: The created_date as `datetime.datetime`
		"""
		if isinstance(self.created_date, str):
			return str_to_datetime(self.created_date)
		return self.created_date
