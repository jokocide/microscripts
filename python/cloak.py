#!/usr/bin/python3
import sys

args = sys.argv
file_name = args[1]
files = args[2:]
target = open(file_name, 'a')

print(f"Opened {file_name} and appended:")
for file in files:
    target.write(file+ '\n')
    print(f"\t- {file}")
target.close()