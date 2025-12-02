with open(".\\2025\\02\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def id_checker(id):
    id_length = len(str(id))
    if id_length % 2 == 0 and str(id)[0:int(id_length / 2)] == str(id)[int(id_length / 2):]:
        return True

sum_invalid_ids = 0        

for line in inputs.split(","):
    begin_range, end_range = map(int, line.split("-"))
    for id in range(begin_range, end_range + 1):
        if id_checker(id):
            sum_invalid_ids += id

print(sum_invalid_ids)