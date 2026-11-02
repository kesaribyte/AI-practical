
from collections import deque

def get_neighbors(state, cap_a, cap_b):
    """Generate action and next state pairs."""
    a, b = state

    pour_ab = min(a, cap_b - b)
    pour_ba = min(b, cap_a - a)

    yield "Fill A", (cap_a, b)
    yield "Fill B", (a, cap_b)
    yield "Empty A", (0, b)
    yield "Empty B", (a, 0)
    yield "Pour A->B", (a - pour_ab, b + pour_ab)
    yield "Pour B->A", (a + pour_ba, b - pour_ba)


def is_goal(state, target):
    return target in state


def reconstruct(parent, state):
    path = []

    while parent[state][0] is not None:
        prev, action = parent[state]
        path.append((action, state))
        state = prev

    return path[::-1]


def dfs(cap_a, cap_b, target):
    """Iterative DFS using a stack."""
    start = (0, 0)
    stack = [start]
    parent = {start: (None, None)}
    expanded = 0

    while stack:
        state = stack.pop()
        expanded += 1

        if is_goal(state, target):
            return reconstruct(parent, state), expanded

        for action, nxt in get_neighbors(state, cap_a, cap_b):
            if nxt not in parent:
                parent[nxt] = (state, action)
                stack.append(nxt)

    return None, expanded


def bfs(cap_a, cap_b, target):
    """BFS using a queue."""
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
    CAP_A, CAP_B, TARGET = 4, 3, 2

    path, n = dfs(CAP_A, CAP_B, TARGET)
    show("DFS", path, n)

    path, n = bfs(CAP_A, CAP_B, TARGET)
    show("BFS (for comparison)", path, n)
