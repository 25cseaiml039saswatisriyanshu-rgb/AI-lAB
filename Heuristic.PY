def get_users_inputs():
    heuristic={}
    num_nodes = int(input("enter total number of nodes:"))
    print("\n enter heursitic value  h(n) for each node:")
    for _ in range(num_nodes):
        node= input("node name:").strip().upper()
        h_val = float(input(f" heuristich({node}):"))
        heuristic[node]=h_val
    graph = {node:[]for node in heuristic}
    num_edges = int(input("\n enter the total number of directed edges:"))
    print("\n enter edges in format (from_node to_node weight):")
    for i in range(num_edges):
        u,v,w = input(f"edge{i+1}:").strip().split()
        u,v,=u.upper(),v.upper()
        weight = float(w)
        graph[u].append((v,weight))
    return graph, heuristic
def astar (graph ,heuristic,start,goal):
    open_list=[(start,0)]
    came_from={}
    g_cost={start:0}
    while open_list:
        current= min (open_list,key=lambda x:x[1]+heuristic[x[0]])
        open_list.remove(current)
        current_node ={current[0]}
        if current_node==goal:
            path =[goal]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path,g_cost[goal]   
        for neighbour,cost in graph.get(current_node,[]):
            new_cost = g_cost[current_node]+cost
            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour]=new_cost
                came_from[neighbour]=current_node
                open_list.append((neighbour,new_cost))
    return None,float('inf')
if __name__ == "__main__":
    print("=== A*Algorithm input setup ===\n")
    graph,heuristic = get_users_inputs()
    print("\n---- path finding----")
    start = input ("enter start node:").strip().upper()
    goal = input("enter goal node").strip().upper()
    path,cost = astar(graph ,heuristic,start,goal)
    print("\n===Result===")
    if path :
        print("shortest path:","->".join(path))
        print("total path cost:",cost)
    else:
        print("path not found")
        
    
    
                               