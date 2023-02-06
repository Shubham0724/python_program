#JSON
#JSON stands for JavaScript Object Notation. It is a built-in package provided in python that is used to store and exchange data.

#A. Converting JSON string to python:

import json

# JSON String:
colors =  '["Red", "Yellow", "Green", "Blue"]'

# JSON string to python dictionary:
lst1 = json.loads(colors)
print(lst1)

#B. Converting python to JSON string:
import json

# python dictionary
lst1 = ['Red', 'Yellow', 'Green', 'Blue']

# Convert Python dict to JSON
jsonObj = json.dumps(lst1)
print(jsonObj)

#C. Conversion type:
import json

print(json.dumps(22))               #integer
print(json.dumps(6.022))            #float
print(json.dumps("Hello World"))    #string
print(json.dumps(True))             #True
print(json.dumps(False))            #False
print(json.dumps(None))             #None