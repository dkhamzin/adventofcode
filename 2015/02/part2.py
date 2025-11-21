with open(".\\2015\\02\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

ribbon = 0
for line in inputs.splitlines():
    l, w, h = map(int, line.split("x"))
    sortedDimensions = sorted([l, w, h])
    wrap = 2 * (sortedDimensions[0] + sortedDimensions[1])
    bow = l * w * h
    ribbon += wrap + bow

print(ribbon)
