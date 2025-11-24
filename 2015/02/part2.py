with open(".\\2015\\02\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

ribbon = 0
for line in inputs.splitlines():
    l, w, h = map(int, line.split("x"))
    sorted_dimensions = sorted([l, w, h])
    wrap = 2 * (sorted_dimensions[0] + sorted_dimensions[1])
    bow = l * w * h
    ribbon += wrap + bow

print(ribbon)
