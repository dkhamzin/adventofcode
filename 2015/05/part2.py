with open(".\\2015\\05\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

niceString = 0

for line in inputs.splitlines():
    pairCheck = False
    repeatCheck = False

    for i in range(len(line) - 1):
        pair = line[i:i+2]
        if line.count(pair) >= 2:
            # Ensure pairs do not overlap
            first_index = line.find(pair)
            second_index = line.find(pair, first_index + 2)
            if second_index != -1:
                pairCheck = True

        if i < len(line) - 2:
            if line[i] == line[i + 2]:
                repeatCheck = True

    if pairCheck and repeatCheck:
        niceString += 1

print(niceString)
