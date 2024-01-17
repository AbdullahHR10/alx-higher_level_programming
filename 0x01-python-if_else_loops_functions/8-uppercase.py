#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for char in str:
        if 'a' <= char <= 'z':
            str2 += chr(ord(char) - ord('a') + ord('A'))
        else:
            str2 += char
