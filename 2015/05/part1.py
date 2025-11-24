with open(".\\2015\\05\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

nice_string = 0

for line in inputs.splitlines():
    vow_check = False
    double_check = False
    seq_check = True
    vowCount = 0

    for i in range(len(line)):
        if line[i] in "aeiou":
            vowCount += 1
        if i < len(line) - 1:
            if line[i] == line[i + 1]:
                double_check = True
            if line[i:i+2] in ["ab", "cd", "pq", "xy"]:
                seq_check = False

    if vowCount >= 3:
        vow_check = True

    if vow_check and double_check and seq_check:
        nice_string += 1

print(nice_string)
