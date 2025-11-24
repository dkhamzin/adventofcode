import hashlib

with open(".\\2015\\04\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

for i in range(1000000):
    test_string = inputs + str(i)
    result = hashlib.md5(test_string.encode())
    hash_string = result.hexdigest()

    if hash_string[0:5] == "00000":
        print(i)
        break
