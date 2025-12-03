with open(".\\2025\\03\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

total_output = 0

def get_output(line):
    max_output = 0
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            current_output = int(line[i] + line[j])
            #print(f"Trying combination: {line[i]} and {line[j]} = {current_output}")
            if current_output > max_output:
                max_output = current_output
    return max_output
    
total_output = 0

for line in inputs.splitlines():
    total_output += get_output(line)

print(total_output)