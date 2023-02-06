#Remove List Items

#1) pop()

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list
print(colors)

#2)remove():
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.remove("blue")
print(colors)

#3)del:
colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)

#4) clear()
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)


##List Comprehension
names = ["compton", "LA", "atlanta", "Pune", "Mumbai"]
namesWith_O = [item for item in names if "e" in item]
print(namesWith_O)
