from collections import deque

def get_neighbors(state, cap_a, cap_b):
"""Generate (action, next_state) pairs from state (a, b)."""
a, b = state
pour_ab = min(a, cap_b - b) # amount moved from A to B
pour_ba = min(b, cap_a - a) # amount moved from B to A
yield "Fill A", (cap_a, b)
yield "Fill B", (a, cap_b)
yield "Empty A", (0, b)
yield "Empty B", (a, 0)
yield f"Pour A->B", (a - pour_ab, b + pour_ab)
yield f"Pour B->A", (a + pour_ba, b - pour_ba)

def is_goal(state, target):
return target in state

def dfs(cap_a, cap_b, target):
"""Iterative DFS using an explicit stack (LIFO)."""
start = (0, 0)
stack = [start]
parent = {start: (None, None)} # also serves as the visited set
expanded = 0

while stack:
state = stack.pop() # LIFO -> go deep first
expanded += 1

if is_goal(state, target):
return reconstruct(parent, state), expanded

for action, nxt in get_neighbors(state, cap_a, cap_b):
if nxt not in parent:
parent[nxt] = (state, action)
stack.append(nxt)

return None, expanded

def bfs(cap_a, cap_b, target):
"""BFS for comparison: guarantees the shortest plan."""
start = (0, 0)
queue = deque([start])
parent = {start: (None, None)}
expanded = 0
while queue:
state = queue.popleft()
expanded += 1
if is_goal(state, target):
return reconstruct(parent, state), expanded
for action, nxt in get_neighbors(state, cap_a, cap_b):
if nxt not in parent:
parent[nxt] = (state, action)
queue.append(nxt)
return None, expanded

def reconstruct(parent, state):

path = []
while parent[state][0] is not None:
prev, action = parent[state]
path.append((action, state))
state = prev
return path[::-1]

def show(name, result, expanded):
print(f"--- {name} ---")
if result is None:
print("No solution\n")
return
print("Start: (0, 0)")
for action, state in result:
print(f" {action:<9} -> {state}")
print(f"Steps: {len(result)}, nodes expanded: {expanded}\n")

if __name__ == "__main__":
CAP_A, CAP_B, TARGET = 4, 3, 2 # 4L and 3L jugs, measure 2L

path, n = dfs(CAP_A, CAP_B, TARGET)
show("DFS", path, n)

path, n = bfs(CAP_A, CAP_B, TARGET)
show("BFS (for comparison)", path, n)
