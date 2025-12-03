with open(".\\2025\\03\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

total_output = 0

def get_output(line):
    stack = []
    to_pick = 12
    for i, digit in enumerate(line):
        remaining = len(line) - i
        while stack and digit > stack[-1] and len(stack) + remaining > to_pick:
            stack.pop()
        if len(stack) < to_pick:
            stack.append(digit)
    return int(''.join(stack))


total_output = 0

for line in inputs.splitlines():
    total_output += get_output(line)

print(total_output)