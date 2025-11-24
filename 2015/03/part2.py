with open(".\\2015\\03\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

coords = (0,0)

coords_type = {
    "santa": (0,0),
    "robo-santa": (0,0)
}

coords_dict = {coords: 1}

i = 0
for char in inputs:
    if i % 2 == 0:
        mover = "santa" 
    else:
        mover = "robo-santa"

    if char == ">" :
        coords_type[mover] = (coords_type[mover][0] + 1, coords_type[mover][1])
    elif char == "<" :
        coords_type[mover] = (coords_type[mover][0] - 1, coords_type[mover][1])
    elif char == "^" :
        coords_type[mover] = (coords_type[mover][0], coords_type[mover][1] + 1)
    elif char == "v" :
        coords_type[mover] = (coords_type[mover][0], coords_type[mover][1] - 1)

    coords_dict[coords_type[mover]] = 1

    i += 1

print(len(coords_dict))
