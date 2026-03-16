from collections import deque

# number of nodes
n = int(input("Enter number of nodes: "))

# adjacency matrix input
print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter start node: "))
goal = int(input("Enter goal node: "))

visited = [False]*n
queue = deque()

queue.append(start)
visited[start] = True

print("\nBFS Traversal with Queue Status:\n")

while queue:
    print("Queue:", list(queue))   # show queue content
    
    node = queue.popleft()
    print("Visited:", node)

    if node == goal:
        print("Goal Found!")
        break

    for i in range(n):
        if graph[node][i] == 1 and not visited[i]:
            queue.append(i)
            visited[i] = True