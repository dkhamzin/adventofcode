with open(".\\2015\\07\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def line_parser(line):
    parts = line.split(" ")

    inputSignal2 = 0
    if len(parts) == 3:
        inputSignal1 = parts[0]
        operation = "ASSIGN"
        outputSignal = parts[2] 

    if len(parts) == 4:
        operation = parts[0]  #NOT
        inputSignal1 = parts[1]
        outputSignal = parts[3]

    if len(parts) == 5:
        inputSignal1 = parts[0]
        operation = parts[1]  #AND, OR, LSHIFT, RSHIFT
        inputSignal2 = parts[2]
        outputSignal = parts[4]

    return operation, inputSignal1, inputSignal2, outputSignal 

signals = {}

for line in inputs.splitlines():
    operation, inputSignal1, inputSignal2, outputSignal = line_parser(line)
    signals[outputSignal] = [operation, inputSignal1, inputSignal2]

def get_signal(signal):
    if signal.isdigit():
        return int(signal)
    
    operation, inputSignal1, inputSignal2 = signals[signal]

    if operation == "ASSIGN":
        value = get_signal(inputSignal1)
    elif operation == "NOT":
        value = ~get_signal(inputSignal1) & 0xFFFF
    elif operation == "AND":
        value = get_signal(inputSignal1) & get_signal(inputSignal2)
    elif operation == "OR":
        value = get_signal(inputSignal1) | get_signal(inputSignal2)
    elif operation == "LSHIFT":
        value = (get_signal(inputSignal1) << get_signal(inputSignal2)) & 0xFFFF
    elif operation == "RSHIFT":
        value = get_signal(inputSignal1) >> get_signal(inputSignal2)
    else:
        value = inputSignal1

    signals[signal] = ["VALUE", value, value]  #cache the computed value
    return value

print(get_signal("a"))
