with open(".\\2025\\07\\inputdemo.txt", "r", encoding="utf-8") as file:
    inputs = file.read()

lines = inputs.splitlines()

lines_list = [list(line) for line in lines]
tree = {}

route_counts = {}

for line_index in range(len(lines_list) - 1):
    for char_index in range(len(lines_list[line_index])):
        if lines_list[line_index][char_index] in "S|":
            if lines_list[line_index + 1][char_index] == ".":
                lines_list[line_index + 1][char_index] = "|"
                tree[(line_index, char_index)] = [(line_index + 1, char_index)]
            elif lines_list[line_index + 1][char_index] == "^":
                lines_list[line_index + 1][char_index - 1] = "|"
                lines_list[line_index + 1][char_index + 1] = "|"
                tree[(line_index, char_index)] = [(line_index + 1, char_index - 1), (line_index + 1, char_index + 1)]
            else:
                tree[(line_index, char_index)] = [(line_index + 1, char_index)]

def find_all_paths(tree, root):
    memo = {}

    def dfs(node):
        if node in memo:
            return memo[node]

        if node not in tree or not tree[node]:  # Leaf node
            memo[node] = [[node]]
            return memo[node]

        paths = []
        for child in tree[node]:
            for subpath in dfs(child):
                paths.append([node] + subpath)

        memo[node] = paths
        return paths

    return dfs(root)

root = sorted(tree.keys())[0]

all_paths = find_all_paths(tree, root)

print(len(all_paths))
