with open(".\\2015\\05\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

niceString = 0

for line in inputs.splitlines():
    vowCheck = False
    doubleCheck = False
    seqCheck = True
    vowCount = 0

    for i in range(len(line)):
        if line[i] in "aeiou":
            vowCount += 1
        if i < len(line) - 1:
            if line[i] == line[i + 1]:
                doubleCheck = True
            if line[i:i+2] in ["ab", "cd", "pq", "xy"]:
                seqCheck = False

    if vowCount >= 3:
        vowCheck = True

    if vowCheck and doubleCheck and seqCheck:
        niceString += 1

print(niceString)
