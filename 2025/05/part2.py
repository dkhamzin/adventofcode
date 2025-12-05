with open(".\\2025\\05\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

id_db = set()

for line in inputs.splitlines():
    if "-" in line:
        begin_range, end_range = map(int,line.split("-"))
        id_range = (begin_range, end_range)
        id_db.add(id_range)

id_db_sorted = sorted(id_db)

changed = True
while changed:
    changed = False
    for i in range(len(id_db_sorted) - 1):
        current_range = id_db_sorted[i]
        next_range = id_db_sorted[i + 1]
        if current_range[1] >= next_range[0] - 1:
            if current_range[1] >= next_range[1]:
                del id_db_sorted[i + 1]
            else:            
                new_range = (min(current_range[0], next_range[0]), max(current_range[1], next_range[1]))
                id_db_sorted[i] = new_range
                del id_db_sorted[i + 1]
            changed = True
            break
                
fresh_count = 0
for i in range(len(id_db_sorted)):
    fresh_count += id_db_sorted[i][1] - id_db_sorted[i][0] + 1

print(fresh_count)