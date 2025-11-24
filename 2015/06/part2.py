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
        start_coords = parts[2]
        end_coords = parts[4]
    elif parts[0] == "toggle":
        action = "toggle"
        start_coords = parts[1]
        end_coords = parts[3]

    start_x, start_y = map(int, start_coords.split(","))
    end_x, end_y = map(int, end_coords.split(","))

    return action, start_x, start_y, end_x, end_y


for line in inputs.splitlines():
    action, start_x, start_y, end_x, end_y = line_parser(line)

    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if action == "on":
                grid[(x,y)] += 1
            elif action == "off":
                if grid[(x,y)] > 0:
                    grid[(x,y)] -= 1
            elif action == "toggle":
                grid[(x,y)] += 2

total_brightness = sum(grid.values())
print(total_brightness)
