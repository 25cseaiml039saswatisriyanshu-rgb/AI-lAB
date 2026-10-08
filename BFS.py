#Experiment:-01
def bfs(student_graph, start):
    visited = []
    queue = [start]
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print("Exploring node:", current_node)
            visited.append(current_node)
            for neighbor in student_graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited
print("---Building Graph---")
student_graph = {}
num_edges = int(input("How many edges (connections) does your graph have? = "))
print("Enter each edge separated by a space (e.g., A B):")
for i in range(num_edges):
    u, v = input(f"Edge {i+1}: ").split()
    if u not in student_graph:
        student_graph[u] = []
    if v not in student_graph:
        student_graph[v] = []
    student_graph[u].append(v)
    student_graph[v].append(u)
start = input("Enter the starting node for BFS: ")
print(f"\nYour Graph Dictionary: {student_graph}")
print("Starting BFS Traversal....")
bfs(student_graph, start)