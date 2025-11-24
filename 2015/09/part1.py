import itertools

with open(".\\2015\\09\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def line_parser(line):
    parts = line.split(" ")
    start_node = parts[0]
    end_node = parts[2]
    distance = int(parts[4])
    return start_node, end_node, distance

nodes = set()
distances = {}


for line in inputs.splitlines():
    start_node, end_node, distance = line_parser(line)
    nodes.add(start_node)
    nodes.add(end_node)
    distances[(start_node, end_node)] = distance
    distances[(end_node, start_node)] = distance

min_distance = None

for chain in itertools.permutations(nodes):
    total_distance = 0
    for i in range(len(chain) - 1):
        total_distance += distances[(chain[i], chain[i+1])]
    if min_distance is None or total_distance < min_distance:
        min_distance = total_distance

print(min_distance)