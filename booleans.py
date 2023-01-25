#examples where the Boolean returns True/False values for different datatypes.

#None:
print("None: ",bool(None))

#numbers
print("Zero:",bool(0))
print("Integer:",bool(23))
print("Float:",bool(3.142))
print("Complex:",bool(5+2j))


#Strings
print("Any string:",bool("central"))   
print("A string containing number:",bool("8.5"))      
print("Empty string:" ,"") 

# Lists:
print("Empty List:",bool([]))
print("List:",bool([1,2,5,2,1,3]))


#Tuples
print("Empty Tuple:",bool(()))
print("Tuple:",bool(("Horse", "Rhino", "Tiger")))

#Sets and Dictionaries:
print("Empty Dictionary:",bool({}))
print("Empty Set:",bool({"Mike", 22, "Science"}))
print("Dictionary:",bool({"name":"Lakshmi", "age":24 ,"job":"unemployed"}))