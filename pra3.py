
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    """Calculate Manhattan distance heuristic."""
    dist = 0

    for i, tile in enumerate(state):
        if tile != 0:
            goal_i = GOAL.index(tile)
            dist += abs(i // 3 - goal_i // 3) + abs(i % 3 - goal_i % 3)

    return dist


def get_neighbors(state):
    """Generate neighboring states by sliding the blank."""
    neighbors = []
    b = state.index(0)
    row, col = b // 3, b % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            n = r * 3 + c
            new = list(state)
            new[b], new[n] = new[n], new[b]
            neighbors.append(tuple(new))

    return neighbors


def astar(start):
    open_list = [(manhattan(start), 0, start, [start])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == GOAL:
            return path

        if state in visited:
            continue

        visited.add(state)

        for nxt in get_neighbors(state):
            if nxt not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(nxt)
                heapq.heappush(
                    open_list,
                    (new_f, new_g, nxt, path + [nxt])
                )

    return None


def print_board(state):
    for i in range(0, 9, 3):
        print(*[x if x != 0 else "_" for x in state[i:i + 3]])
    print()


if __name__ == "__main__":
    start = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    solution = astar(start)

    if solution:
        print("Solved in", len(solution) - 1, "moves\n")

        for step, board in enumerate(solution):
            print("Step", step)
            print_board(board)
    else:
        print("No solution exists")
