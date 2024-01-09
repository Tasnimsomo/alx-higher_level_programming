#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
""


def write_file(filename="", text=""):
     """
    Write the specified text to a file (UTF8) and return the number of characters written.

    Parameters:
    - filename (str): The name or path of the file to be written.
    - text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename,mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
