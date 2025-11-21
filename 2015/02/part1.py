with open(".\\2015\\02\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

total_area = 0
for line in inputs.splitlines():
    l, w, h = map(int, line.split("x"))
    side1 = l * w
    side2 = w * h
    side3 = h * l
    surface_area = 2 * (side1 + side2 + side3)
    slack = min(side1, side2, side3)
    total_area += surface_area + slack

print(total_area)
