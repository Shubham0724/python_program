#Binary data: 

#bytes

#Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1, 'utf-8')
print(arr1)
arr2 = bytes(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytes(4)
print(bytestr)

#bytearray

#Converting string to bytes
str1 = "This is a string"
arr1 = bytearray(str1, 'utf-8')
print(arr1)
arr2 = bytearray(str1, 'utf-16')
print(arr2)

#Creating bytes of given size
bytestr = bytearray(4)
print(bytestr)

#memoryview

str1 = bytes("home", "utf-8")
memoryviewstr = memoryview(str1)
print(list(memoryviewstr[0:]))

#set data

set1 = {4, -5, 8, 3, 2.9}
print(set1)

#None

state = None
print(type(state))