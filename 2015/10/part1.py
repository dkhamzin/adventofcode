with open(".\\2015\\10\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

class LookAndSayIterator:
    def __init__(self, input_string):
        self.current_string = input_string

    def __iter__(self):
        return self

    def __next__(self):
        result = ""
        i = 0
        while i < len(self.current_string):
            count = 1
            while i + 1 < len(self.current_string) and self.current_string[i] == self.current_string[i + 1]:
                count += 1
                i += 1
            result += str(count) + self.current_string[i]
            i += 1
        self.current_string = result
        return self.current_string

look_and_say_iterator_instance = LookAndSayIterator(inputs.strip())
for _ in range(40):
    next(look_and_say_iterator_instance)
print(len(look_and_say_iterator_instance.current_string))
