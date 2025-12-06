with open(".\\2025\\06\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

lines = inputs.splitlines()

problem_list = lines[-1].split()

total_sum = 0

for problem_index in range(len(problem_list)):
    problem_type = problem_list[problem_index]

    problem_add = 0
    problem_mult = 1

    for line_index in range(len(lines) - 1):
        line_split = lines[line_index].split()
        if problem_type == "*":
            problem_mult *= int(line_split[problem_index])
        elif problem_type == "+":
            problem_add += int(line_split[problem_index])

    if problem_mult == 1:
        problem_mult = 0
    total_sum += problem_add + problem_mult

print(total_sum)