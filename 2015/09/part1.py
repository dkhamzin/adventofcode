import itertools

with open(".\\2015\\09\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

def line_parser(line):
    parts = line.split(" ")
    startNode = parts[0]
    endNode = parts[2]
    distance = int(parts[4])
    return startNode, endNode, distance

nodes = set()
distances = {}


for line in inputs.splitlines():
    startNode, endNode, distance = line_parser(line)
    nodes.add(startNode)
    nodes.add(endNode)
    distances[(startNode, endNode)] = distance
    distances[(endNode, startNode)] = distance

minDistance = None

for chain in itertools.permutations(nodes):
    totalDistance = 0
    for i in range(len(chain) - 1):
        totalDistance += distances[(chain[i], chain[i+1])]
    if minDistance is None or totalDistance < minDistance:
        minDistance = totalDistance

print(minDistance)