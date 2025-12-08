with open(".\\2025\\06\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

lines = inputs.splitlines()

#find problem indexies
problem_indexies = []
for problem_index in range(len(lines[-1])):
    if any([lines[-1][problem_index] == "*", lines[-1][problem_index] == "+"]):
        problem_indexies.append(problem_index)

total_sum = 0

for problem_index in range(len(problem_indexies)):
    problem_type = lines[-1][problem_indexies[problem_index]]
    begin_range = problem_indexies[problem_index]
    if problem_index + 1 < len(problem_indexies):
        end_range = problem_indexies[problem_index + 1] - 1
    else:
        end_range = len(lines[-1])

    length = end_range - begin_range

    cef_problem = []

    for line in lines[:-1]:
        #extract cef problem
        current_problem = line[begin_range:end_range]
        for digit_index in range(length):
            if len(cef_problem) < length:
                cef_problem.append(current_problem[digit_index])
            else:
                cef_problem[digit_index] += current_problem[digit_index]

    #finally calculate the result
    if problem_type == "*":
        problem_mult = 1
        for digit_str in cef_problem:
            problem_mult *= int(digit_str)
        total_sum += problem_mult
    elif problem_type == "+":
        problem_add = 0
        for digit_str in cef_problem:
            problem_add += int(digit_str)
        total_sum += problem_add

print(total_sum)
