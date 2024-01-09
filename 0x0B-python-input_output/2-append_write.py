#!/usr/bin/python3
'''module that appends text'''


def append_write(filename="", text=""):
    """
    Append the specified text to the end of a file.

    Parameters:
    - filename (str): The name of the file.
    - text (str): The text to be appended.

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
