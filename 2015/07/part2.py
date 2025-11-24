with open(".\\2015\\07\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def line_parser(line):
    parts = line.split(" ")

    input_signal2 = 0
    if len(parts) == 3:
        input_signal1 = parts[0]
        operation = "ASSIGN"
        output_signal = parts[2]

    if len(parts) == 4:
        operation = parts[0]  #NOT
        input_signal1 = parts[1]
        output_signal = parts[3]

    if len(parts) == 5:
        input_signal1 = parts[0]
        operation = parts[1]  #AND, OR, LSHIFT, RSHIFT
        input_signal2 = parts[2]
        output_signal = parts[4]

    return operation, input_signal1, input_signal2, output_signal 

signals = {}

def read_signals():
    for line in inputs.splitlines():
        operation, input_signal1, input_signal2, output_signal = line_parser(line)
        signals[output_signal] = [operation, input_signal1, input_signal2]

read_signals()
def get_signal(signal):
    if signal.isdigit():
        return int(signal)
    
    operation, input_signal1, input_signal2 = signals[signal]

    if operation == "ASSIGN":
        value = get_signal(input_signal1)
    elif operation == "NOT":
        value = ~get_signal(input_signal1) & 0xFFFF
    elif operation == "AND":
        value = get_signal(input_signal1) & get_signal(input_signal2)
    elif operation == "OR":
        value = get_signal(input_signal1) | get_signal(input_signal2)
    elif operation == "LSHIFT":
        value = (get_signal(input_signal1) << get_signal(input_signal2)) & 0xFFFF
    elif operation == "RSHIFT":
        value = get_signal(input_signal1) >> get_signal(input_signal2)
    else:
        value = input_signal1

    signals[signal] = ["VALUE", value, value]  #cache the computed value
    return value

a_value = get_signal("a")
print("original a value: " + str(a_value))
read_signals()
signals["b"] = ["VALUE", a_value, a_value]  #override b with a's value

print("new a value: " + str(get_signal("a")))