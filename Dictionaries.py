#example
info = {'name':'central', 'age':19, 'eligible':True}
print(info)

#Accessing Dictionary items:
 
#1)Accessing single values:

info = {'name':'central', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

#2)Accessing multiple values:
info = {'name':'Central', 'age':19, 'eligible':True}
print(info.values())

#3)Accessing keys:
info = {'name':'Central', 'age':19, 'eligible':True}
print(info.keys())

#4)Accessing key-value pairs:
info = {'name':'central', 'age':19, 'eligible':True}
print(info.items())

##Adding items to dictionary:

#Create a new key and assign a value to it:

info = {'name':'central', 'age':19, 'eligible':True}
print(info)
info['DOB'] = 2001
print(info)

#Use the update() method:
info = {'name':'central', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

##Removing items from dictionary:

#clear(): The clear() method removes all the items from the list. 

info = {'name':'central', 'age':19, 'eligible':True}
info.clear()
print(info)

#pop(): The pop() method removes the key-value pair whose key is passed as a parameter.

info = {'name':'central', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#popitem(): The popitem() method removes the last key-value pair from the dictionary.

info = {'name':'Central', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

