import hashlib

with open(".\\2015\\04\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

for i in range(10000000):
    testString = inputs + str(i)
    result = hashlib.md5(testString.encode())
    hashString = result.hexdigest()

    if hashString[0:6] == "000000":
        print(i)
        break
