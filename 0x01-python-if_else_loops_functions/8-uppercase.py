#!/usr/bin/python3
def uppercase(s):
    for char in s:
        print("{:c}".format(ord(char) - 32) if 'a' <= char <= 'z' else char, end="")
    print()
