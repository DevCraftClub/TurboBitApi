import os
from datetime import datetime
from typing import Union

ENV_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")


def toint(value: Union[str, int, float]) -> int:
	"""
	The toint function takes a string, int or float and converts it to an integer.

	**Args**:

	`value`: Value as integer, float or string


	**return**: An int
	"""
	return int(float(value))


def str_to_datetime(date_string: str, format_string: str = '%y-%m-%d %H:%M:%S'):
	"""
	The str_to_datetime function takes a string and converts it to a datetime object.

	**Args**:

	`date_string`: str: Specify the date string to be converted. Must be by default in the format '%y-%m-%d %H:%M:%S' or else an error will occur.

	`format_string`: str: Specify the format of the date_string


	**return**: A datetime object
	"""
	return datetime.strptime(date_string, format_string)
