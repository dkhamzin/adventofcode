with open(".\\2015\\06\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

#set lights status to off
grid = {}
for x in range(1000):
    for y in range(1000):
        grid[(x,y)] = 0

def line_parser(line):
    parts = line.split(" ")
    if parts[0] == "turn":
        action = parts[1]  #on or off
        startCoords = parts[2]
        endCoords = parts[4]
    elif parts[0] == "toggle":
        action = "toggle"
        startCoords = parts[1]
        endCoords = parts[3]

    startX, startY = map(int, startCoords.split(","))
    endX, endY = map(int, endCoords.split(","))

    return action, startX, startY, endX, endY


for line in inputs.splitlines():
    action, startX, startY, endX, endY = line_parser(line)

    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if action == "on":
                grid[(x,y)] += 1
            elif action == "off":
                if grid[(x,y)] > 0:
                    grid[(x,y)] -= 1
            elif action == "toggle":
                grid[(x,y)] += 2

totalBrightness = sum(grid.values())
print(totalBrightness)
