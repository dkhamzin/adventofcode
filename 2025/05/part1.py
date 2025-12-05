with open(".\\2025\\05\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

id_db = set()

freshCount = 0

def id_check(id):
    #pass
    for begin, end in id_db:
        if begin < id <= end:
            return 1
    return 0

fresh_count = 0

for line in inputs.splitlines():
    if "-" in line:
        begin_range, end_range = map(int,line.split("-"))
        range = (begin_range, end_range)
        id_db.add(range)
    elif line == "":
        pass
    else:
        fresh_count += id_check(int(line))

print(fresh_count)

