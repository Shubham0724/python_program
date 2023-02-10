info = {"Carla", 19, False, 5.9, 19}
print(info)


#Accessing set items:

#using a For loop
info = {"Central", 19, False, 5.9}
for item in info:
    print(item)


##Add iteams to set:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

##Remove items from set:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#There are various other methods to remove items from the set: pop(), del(), clear().

#pop():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

#clear():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)