from collections import defaultdict

with open(".\\2025\\07\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

lines = inputs.splitlines()

lines_list = [list(line) for line in lines]

route_counts = defaultdict(int)

for line_index in range(len(lines_list) - 1):
    for char_index in range(len(lines_list[line_index])):
        if lines_list[line_index][char_index] == "S":
            route_counts[(line_index, char_index)] = 1
        elif lines_list[line_index][char_index] == "^":
            route_counts[(line_index, char_index - 1)] += route_counts[(line_index - 1, char_index)]
            route_counts[(line_index, char_index + 1)] += route_counts[(line_index - 1, char_index)] + route_counts[(line_index - 1, char_index + 1)]
        else:
            route_counts[(line_index, char_index)] = max(route_counts[(line_index - 1, char_index)],route_counts[(line_index, char_index)])

print(sum(val for key, val in route_counts.items() if key[0] == (len(lines_list) - 2)))
