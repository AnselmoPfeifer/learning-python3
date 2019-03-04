import json

# Using with to open and read a file
with open('file.json') as file:
    file = json.load(file)

# Open and Read a file normally
file = open('file.json')
try:
    file.read()
finally:
    file.close()