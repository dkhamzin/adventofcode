with open(".\\2025\\01\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

class Dialer:
    def __init__(self):
        self.position = 50

    def __iter__(self):
        return self

    def __next__(self):
        if self.direction == "L":
            if self.position != 0:
                self.position -= 1
            else:
                self.position = 99
        elif self.direction == "R":
            if self.position != 99:
                self.position += 1
            else:
                self.position = 0
        return self.position

dialer = Dialer()
zero_count = 0

for line in inputs.splitlines():
    direction = line[0]
    steps = line[1:]
    dialer.direction = direction

    for _ in range(int(steps)):
        next(dialer)
        if dialer.position == 0:
            zero_count += 1

print("New password: " + str(zero_count))