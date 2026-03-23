# IDDFS using stack with adjacency matrix

def dls(matrix, nodes, start, goal, limit):
    stack = [(start, 0)]   # (node_index, depth)
    visited = set()

    while stack:
        current, depth = stack.pop()

        if current not in visited:
            print(nodes[current], end=" ")
            visited.add(current)

            if current == goal:
                return True

            if depth < limit:
                # Traverse neighbors (reverse order for correct DFS order)
                for i in range(len(nodes)-1, -1, -1):
                    if matrix[current][i] == 1:
                        stack.append((i, depth + 1))

    return False


def iddfs(matrix, nodes, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Level {depth}: ", end="")
        if dls(matrix, nodes, start, goal, depth):
            print("\nGoal found!")
            return
    print("\nGoal not found within depth limit.")


# ----------- USER INPUT -----------

n = int(input("Enter number of nodes: "))

# Node names
nodes = []
for i in range(n):
    node = input(f"Enter node {i+1}: ")
    nodes.append(node)

# Adjacency matrix input
print("\nEnter adjacency matrix (row-wise):")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Input start and goal
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")
max_depth = int(input("Enter maximum depth: "))

# Convert node names to index
start = nodes.index(start_node)
goal = nodes.index(goal_node)

# ----------- FUNCTION CALL -----------
iddfs(matrix, nodes, start, goal, max_depth)