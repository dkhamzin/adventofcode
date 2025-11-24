with open(".\\2015\\11\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def increment_pwd(pwd):
    pwd = list(pwd.lower())  # Ensure lowercase
    i = len(pwd) - 1

    while i >= 0:
        if pwd[i] == 'z':
            pwd[i] = 'a'
            i -= 1
        else:
            pwd[i] = chr(ord(pwd[i]) + 1)
            return ''.join(pwd)
    
    return 'a' + ''.join(pwd)

def is_valid(pwd):
    # Condition 1: Does not contain forbidden symbols
    forbidden_symbols = "iol"
    if any(char in forbidden_symbols for char in pwd):
        return False

    # Condition 2: Contains at least one increasing straight of three letters
    has_straight = any(
        ord(pwd[i]) + 1 == ord(pwd[i + 1]) and ord(pwd[i + 1]) + 1 == ord(pwd[i + 2])
        for i in range(len(pwd) - 2)
    )
    if not has_straight:
        return False

    # Condition 3: Contains at least two different non-overlapping pairs
    pairs = set()
    i = 0
    while i < len(pwd) - 1:
        if pwd[i] == pwd[i + 1]:
            pairs.add(pwd[i])
            i += 2  # Skip the next character to avoid overlapping pairs
        else:
            i += 1
    if len(pairs) < 2:
        return False

    return True

def return_next_valid_pwd(pwd):
    test_pwd = increment_pwd(pwd)
    while is_valid(test_pwd) == False:
        test_pwd = increment_pwd(test_pwd)
    return test_pwd

print(return_next_valid_pwd(return_next_valid_pwd(inputs.strip())))