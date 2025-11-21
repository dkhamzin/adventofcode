with open(".\\2015\\03\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

coords = (0,0)

coordsType = {
    "santa": (0,0),
    "robo-santa": (0,0)
}

coordsDict = {coords: 1}

i = 0
for char in inputs:
    if i % 2 == 0:
        mover = "santa" 
    else:
        mover = "robo-santa"

    if char == ">" :
        coordsType[mover] = (coordsType[mover][0] + 1, coordsType[mover][1])
    elif char == "<" :
        coordsType[mover] = (coordsType[mover][0] - 1, coordsType[mover][1])
    elif char == "^" :
        coordsType[mover] = (coordsType[mover][0], coordsType[mover][1] + 1)
    elif char == "v" :
        coordsType[mover] = (coordsType[mover][0], coordsType[mover][1] - 1)

    coordsDict[coordsType[mover]] = 1

    i += 1

print(len(coordsDict))
