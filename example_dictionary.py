thisdict = {
    "brand" : "Ford",
    "electric" : False,
    "model" : "Mustang",
    "year" : 1964,
    "colors" : ["red", "white", "blue"]

}
print(thisdict)

print(thisdict["brand"])
print(len(thisdict))

x = thisdict.get("colors")

print(x)

y = thisdict.keys()
print(y)

car = {
    "Cordell" : "Ford F150",
    "Felicia" : "Ford Fusion",
    "Cameron" : "Dodge Journey",
    "Charley" : "Hyundia Accent"
}

z = car.keys()

print(z)

a = car.values()
print(a)

b = car.items()
print(b)

car["Cordell Jr"] = "Ford Fiesta"

print(b)

if "Charley" in car:
    print("Charley's car is a ", car["Charley"])

if "Shirley" in car:
    print("Yes, Shirley's car is in dictionary.")
else:
    print("Shirley's car is not in the list.")    
