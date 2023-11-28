#!/usr/bin/python3
print(
    "{:c}".format(ord(char) - 32)
    if 'a' <= char <= 'z' else char,
    end=""
)
