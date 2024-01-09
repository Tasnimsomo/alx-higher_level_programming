#!/usr/bin/python3
'''module that converts to json'''
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Parameters:
    - my_obj: The Python object to be converted.

    Returns:
    - str: The JSON-formatted string representing the input Python object.
    """
    text = json.dumps(my_obj)
    return text
