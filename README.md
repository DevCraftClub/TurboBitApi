# Unofficial StreamTape API wrapper

It is a simple API wrapper for the streaming service streamtape.com. The API documentation can be found on the [docs page](https://devcraftclub.github.io/TurboBitApi/). The whole structure of the API has been split into different classes for easy overview and usage.

## Installation

Install with

```python3
pip install turbobit_api
```

## Usage

### General usage

Every class starts with following initialization:

```python3
my_var = selectedClass()
```

Or

```python3
my_var = selectedClass("API Key")
```

### Variables

Put in your environment variable `TURBOBIT_API` like you can see in .env file

Alternatively you can pass the key when class is initialized


### Main classes

#### FileManager

_file: FileManager.py_

Contains functions for working with files and folders. All work with files and folders through the API is done with this class.

#### Remote

_file: Remote.py_

Contains functions to work with remote uploading of files.

#### UploadFile

_file: Upload.py_

The main class for uploading files to turbobit via API


## Changelog

### 1.0.0

- Initial release   
