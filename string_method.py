#upper() : The upper() method converts a string to upper case.

str1 = "central cee"
print(str1.upper())

#lower() : The lower() method converts a string to upper case.

str1 = "CENTRAL CEE"
print(str1.lower())

#strip() : The strip() method removes any white spaces before and after the string.

str2 = " Central cee "
print(str2.strip)

#rstrip() : the rstrip() removes any trailing characters.
str3 = "Central !!!"
print(str3.rstrip("!"))


#replace() : the replace() method replaces a string with another string.
str2 = "Central Cei"
print(str2.replace("i", "e"))

#split() : The split() method splits the give string at the specified instance and returns the separated strings as list items.

str2 = "Central Cee"
print(str2.split(" "))      #Splits the string at the whitespace " ".

#capitalize() : The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

str1 = "Central"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "CeNtraL CeE"
capStr2 = str2.capitalize()
print(capStr2)
