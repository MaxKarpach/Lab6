from collections import deque, defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    n = int(lines[0])
    reactions = [line.split("->") for line in lines[1:n+1]]
    start = lines[n+1]
    target = lines[n+2]
    return reactions, start, target

def build_graph(reactions):
    graph = defaultdict(list)
    for source, target in reactions:
        graph[source].append(target)
    return graph

def bfs_shortest_path(graph, start, target):
    if start == target:
        return 0
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        current, depth = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph[current]:
            if neighbor == target:
                return depth + 1
            queue.append((neighbor, depth + 1))
    return -1

def write_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) + '\n')


reactions, start, target = read_input("input.txt")
graph = build_graph(reactions)
result = bfs_shortest_path(graph, start, target)
write_output("output.txt", result)
