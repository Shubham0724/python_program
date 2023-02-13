#Manipulating Tuples
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

##Unpack Tuples
info = ("Marcus", 20, "MIT")
(name, age, university) = info
print("Name:", name)
print("Age:",age)
print("Studies at:",university)