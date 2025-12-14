import itertools
with open(".\\2025\\09\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

coords_list = []
for line in inputs.splitlines():
    x, y = map(int, line.split(","))
    coords_list.append([x,y])


max_rec_square = 0
for rectangle in itertools.permutations(coords_list, 2):
    rec_square = (abs(rectangle[0][0] - rectangle[1][0]) + 1) * (abs(rectangle[0][1] - rectangle[1][1]) + 1)
    if rec_square > max_rec_square:
        max_rec_square = rec_square

print(max_rec_square)