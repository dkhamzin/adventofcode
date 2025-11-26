import json
with open(".\\2015\\12\\input.txt", "r", encoding="utf-8") as file:
    inputs = json.load(file)

def extract_ints(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(extract_ints(item) for item in data)
    elif isinstance(data, dict) and "red" not in data.values():
        return sum(extract_ints(value) for value in data.values())
    else:
        return 0

print(extract_ints(inputs))
