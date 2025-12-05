with open(".\\2025\\04\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()


lines = inputs.splitlines()
rows = len(lines) + 2
cols = len(lines[0]) + 2

a = [[0]*cols for _ in [0]*rows]

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        a[i][j] = lines[i - 1][j - 1]    


def count_neighbors(x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i != x or j != y) and a[i][j] == "@":
                count += 1
    return count

accessible_count = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if a[i][j] == "@" and count_neighbors(i, j) <= 3:
            accessible_count += 1


print(accessible_count)