with open(".\\2015\\08\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

total_difference = 0
for line in inputs.splitlines():
    string_literal_size = len(line)
    in_memory_size = len(line.encode("utf-8").decode("unicode_escape")) - 2

#    print(f"{line}: {string_literal_size}, {in_memory_size}")
    total_difference += string_literal_size - (in_memory_size)

print(total_difference)