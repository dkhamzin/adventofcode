with open(".\\2025\\02\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i

def id_checker(id):
    id_length = len(str(id))
    divisors_list = list(get_divisors(id_length))
    for divisor in divisors_list:
        if all(str(id)[i:i+divisor] == str(id)[0:divisor] for i in range(0, id_length, divisor)):
            return True


sum_invalid_ids = 0        

for line in inputs.split(","):
    begin_range, end_range = map(int, line.split("-"))
    for id in range(begin_range, end_range + 1):
        if id_checker(id):
            sum_invalid_ids += id

print(sum_invalid_ids)