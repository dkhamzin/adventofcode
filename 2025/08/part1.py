import itertools, math
with open(".\\2025\\08\\input.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

coords_list = []

for line in inputs.splitlines():
    coords = line.split(",")
    coords_list.append(coords)

def calc_distance(coords1, coords2):
    x1, y1, z1 = map(int, coords1)
    x2, y2, z2 = map(int, coords2)
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

#add all coords as single circuits
circuits = [[coord] for coord in coords_list]

def find_coord_in_circuits(coord):
    for circuit_index, circuit in enumerate(circuits):
        if coord in circuit:
            return circuit_index, circuit.index(coord)
    return None, None

distances = []
duplicates = set()
for coord1 in coords_list:
    for coord2 in coords_list[1:]:
        str_coords = str((coord1, coord2))
        str_coords_reversed = str((coord2, coord1))
        if coord1 != coord2 and not str_coords in duplicates:
            distances.append([calc_distance(coord1, coord2), [coord1, coord2]])
            duplicates.add(str(str_coords))
            duplicates.add(str(str_coords_reversed))

sorted_distances = sorted(distances)

connection_count = 0
while connection_count < 1000:
    dist, coords = sorted_distances[0]
    sorted_distances.pop(0)
    coord1, coord2 = coords
    coord1_circuit_index, coord1_index = find_coord_in_circuits(coord1)
    coord2_circuit_index, coord2_index = find_coord_in_circuits(coord2)

    if coord1_circuit_index != coord2_circuit_index:
        circuits[coord1_circuit_index] += circuits[coord2_circuit_index]
        circuits.pop(coord2_circuit_index)
    connection_count += 1

circuits_lenghts = sorted(list(len(circuit) for circuit in circuits), reverse=True)

print(circuits_lenghts[0] * circuits_lenghts[1] * circuits_lenghts[2])