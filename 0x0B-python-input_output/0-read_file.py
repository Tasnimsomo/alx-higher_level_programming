#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read the content of a file and print it to the console.

    Parameters:
    - filename (str): The name or path of the file to be read.

    Returns:
    None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
