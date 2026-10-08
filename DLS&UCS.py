from collections import deque

def clear(state, block):
    return not any(pos == block for b, pos in state)

def moves(state, blocks):
    result = []

    for block in blocks:
        pos = next(p for b, p in state if b == block)

        if not clear(state, block):
            continue

        # Move to table
        if pos != "Table":
            s = set(state)
            s.remove((block, pos))
            s.add((block, "Table"))
            result.append((frozenset(s), f"Move {block} from {pos} to Table"))

        # Move onto another block
        for dest in blocks:
            if dest != block and clear(state, dest) and pos != dest:
                s = set(state)
                s.remove((block, pos))
                s.add((block, dest))
                result.append((frozenset(s),
                               f"Move {block} from {pos} to {dest}"))
    return result

def block_world(start, goal, blocks):
    q = deque([(frozenset(start), [])])
    visited = {frozenset(start)}

    while q:
        state, path = q.popleft()

        if state == frozenset(goal):
            return path

        for new_state, move in moves(state, blocks):
            if new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [move]))

    return None

# Main
blocks = ["A", "B", "C"]

start = {("A", "Table"), ("B", "A"), ("C", "Table")}
goal = {("A", "B"), ("B", "C"), ("C", "Table")}

solution = block_world(start, goal, blocks)

print("Initial:", start)
print("Goal:", goal)

if solution:
    print("\nSolution:")
    for i, move in enumerate(solution, 1):
        print(i, move)
    print("Total moves:", len(solution))
else:
    print("No solution")