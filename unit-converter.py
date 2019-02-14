x = input("Distance? ")
u = input("units? ")
if u == "feet":
    y = int(x * 0.3048)
    z = round(y, 5)
    print(z, " m")
elif u == "miles":
    y = int(x * 16039.34)
    z = round(y, 5)
    print(z, " m")
elif u == "yards":
    y = int(x * 0.9144)
    z = round(y, 5)
    print(z, " m")
elif u == "inches":
    y = int(x * 0.0254)
    z = round(y, 5)
    print(z, " m")
else:
    print("Learn to spell!")