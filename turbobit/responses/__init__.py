from typing import Optional


class Response:
	error: bool = False

	@staticmethod
	def error_response(error_msg: str, class_name=None, function_name: Optional[str] = None, **additional_data):
		"""
		The error_response function is used to return a JSON response with an error message.

		The function takes the following arguments:

		- error_msg (str): The error message to be returned in the JSON response.

		- class_name (optional): The name of the class that called this function. Defaults to None if not provided.

		- function_name (str, optional): The name of the function that called this function. Defaults to None if not provided.
		- additional_data (dict, optional): Additional data for better error messages

		**Args**:

		- `error_msg`: str: Pass the error message

		- `class_name`: Identify the class where the error occurred

		- `function_name`: str: Specify the function name (Optional)

		- `**additional_data`: Pass additional data to the error_response function

		**Return**: A dictionary with an error key set to true

		- error: True/False

		- message: Error message or description

		- class_name: Name of the class where error occurred

		- class_name: Name of the class where error occurred

		- function_name: Name of the function where error occurred

		- extra_data: Additional data as dict

		"""
		return {
			'error'        : True,
			'message'      : error_msg,
			'class_name'   : class_name,
			'function_name': function_name,
			'extra_data'   : additional_data
		}
