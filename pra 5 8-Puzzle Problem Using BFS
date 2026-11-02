from collecƟons import deque
GOAL = (1, 2, 3,
4, 5, 6,
7, 8, 0)
def get_neighbors(state):
"""Return (move, new_state) for every legal blank move."""
result = []
b = state.index(0)
row, col = b // 3, b % 3
moves = {"Up": (-1, 0),
"Down": (1, 0),
"LeŌ": (0, -1),
"Right": (0, 1)
}
for name, (dr, dc) in moves.items():
r, c = row + dr, col + dc
if 0 <= r < 3 and 0 <= c < 3:
n = r * 3 + c
new = list(state)
new[b], new[n] = new[n], new[b]
result.append((name, tuple(new)))
return result

def bfs(start):
queue = deque([(start, [])]) # (state, moves taken so far)
visited = {start}

expanded = 0

while queue:
state, path = queue.popleŌ() # FIFO: shallowest state first
expanded += 1

if state == GOAL:
return path, expanded

for move, nxt in get_neighbors(state):
if nxt not in visited:
visited.add(nxt)
queue.append((nxt, path + [move]))
return None, expanded

def print_board(state):
for i in range(0, 9, 3):
print(*[x if x != 0 else "_" for x in state[i:i + 3]])
print()

if __name__ == "__main__":
start = (1, 3, 6,
5, 2, 0,
4, 7, 8)

print("Start state:")
print_board(start)

path, expanded = bfs(start)

if path is None:
print("No soluƟon exists")
else:
print("Moves :", " -> ".join(path))
print("SoluƟon cost:", len(path), "moves")
print("Nodes expanded:", expanded, "\n")

# Replay the plan to show each state
state = start
for step, move in enumerate(path, 1):
for name, nxt in get_neighbors(state):
if name == move:
state = nxt
break
print(f"Step {step}: {move}")
print_board(state)
