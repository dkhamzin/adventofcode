with open(".\\2015\\08\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

total_difference = 0
for line in inputs.splitlines():
    string_literal_size = len(line)
    new_encoded_size = len(line.replace("\\", "\\\\").replace('"', '\\"')) + 2
    total_difference += new_encoded_size - string_literal_size

print(total_difference)