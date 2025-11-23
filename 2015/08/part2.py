with open(".\\2015\\08\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

totalDifference = 0
for line in inputs.splitlines():
    stringLiteralSize = len(line)
    newEncodedSize = len(line.replace("\\", "\\\\").replace('"', '\\"')) + 2
#    print(f"{line}: {stringLiteralSize}, {inMemorySize}")
    totalDifference += newEncodedSize - stringLiteralSize

print(totalDifference)