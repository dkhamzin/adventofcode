with open(".\\2025\\07\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

lines = inputs.splitlines()

lines_list = [list(line) for line in lines]

total_splits = 0

for line_index in range(len(lines_list) - 1):
    for char_index in range(len(lines_list[line_index])):
        if lines_list[line_index][char_index] in "S|":
            if lines_list[line_index + 1][char_index] == ".":
                lines_list[line_index + 1][char_index] = "|"
        elif lines_list[line_index][char_index] == "^":
            if lines_list[line_index - 1][char_index] == "|":
                total_splits += 1
                lines_list[line_index + 1][char_index - 1] = "|"
                lines_list[line_index + 1][char_index + 1] = "|"

print(total_splits)
