with open(".\\2015\\03\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

coords = (0,0)

coordsDict = {coords: 1}

for char in inputs:
    if char == ">" :
        coords = (coords[0] + 1, coords[1])
    elif char == "<" :
        coords = (coords[0] - 1, coords[1])
    elif char == "^" :
        coords = (coords[0], coords[1] + 1)
    elif char == "v" :
        coords = (coords[0], coords[1] - 1)

    coordsDict[coords] = 1

print(len(coordsDict))
