from collections import deque
def water_juge(cap1,cap2,target_state):
    visited=set()
    queue=deque()
    #queue stores (jug1_water,j2,path_hist)
    queue.append((0,0,[]))
    
    while queue:
        j1,j2,path=queue.popleft()
        if (j1,j2) in visited:
            continue
        visited.add((j1,j2))
        
        current_path=path+[(j1,j2)]
        
        if (j1,j2)==target_state:
            return current_path
        next_moves=[
            (cap1,j2),
            (j1,cap2),
            (0,j2),
            (j1,0),
            (j1 - min(j1,cap2-j2),j2+min(j1,cap2-j2)),
            (j1 + min(j1,cap1-j1),j2-min(j1,cap1-j1)),
            
        ]
        
        for move in next_moves:
            if move not in visited:
                queue.append((move[0],move[1],current_path))
    return None

target_goal=(4,2)
solution=water_juge(4,3,target_goal)

if solution:
    print(f"steps to reach target state {target_goal}:")
    for step in solution:
        print(step)
        
else:
    print("no solution exists")
                 