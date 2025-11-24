with open(".\\2015\\10\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

class LookAndSayIterator:
    def __init__(self, inputString):
        self.currentString = inputString

    def __iter__(self):
        return self

    def __next__(self):
        result = ""
        i = 0
        while i < len(self.currentString):
            count = 1
            while i + 1 < len(self.currentString) and self.currentString[i] == self.currentString[i + 1]:
                count += 1
                i += 1
            result += str(count) + self.currentString[i]
            i += 1
        self.currentString = result
        return self.currentString

LookAndSayIteratorInstance = LookAndSayIterator(inputs.strip())
for _ in range(40):
    next(LookAndSayIteratorInstance)
print(len(LookAndSayIteratorInstance.currentString))
