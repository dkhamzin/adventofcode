"""Iterate through the input characters to calculate the final position."""

with open(".\\2015\\01\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

position = 0

for char in inputs:
    if char == "(" :
        position += 1
    else:
        position -= 1

print(position)
