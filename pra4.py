
import math

# Leaf values of a complete binary game tree
# Root = MAX, next level = MIN, next level = MAX, then leaves
values = [3, 5, 6, 9, 1, 2, 0, -1]
MAX_DEPTH = 3

nodes_visited = 0  # Leaves evaluated


def alphabeta(depth, index, is_max, alpha, beta):
    """
    depth: current depth in the tree
    index: index of the node
    is_max: True for MAX, False for MIN
    alpha: best value MAX can guarantee
    beta: best value MIN can guarantee
    """
    global nodes_visited

    # Leaf node
    if depth == MAX_DEPTH:
        nodes_visited += 1
        return values[index]

    if is_max:
        best = -math.inf

        for child in (index * 2, index * 2 + 1):
            val = alphabeta(depth + 1, child, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                print(f"Pruned at depth {depth} (MAX): alpha={alpha}, beta={beta}")
                break

        return best

    else:
        best = math.inf

        for child in (index * 2, index * 2 + 1):
            val = alphabeta(depth + 1, child, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                print(f"Pruned at depth {depth} (MIN): alpha={alpha}, beta={beta}")
                break

        return best


if __name__ == "__main__":
    print("Leaf values:", values, "\n")

    result = alphabeta(0, 0, True, -math.inf, math.inf)

    print("\nOptimal value for MAX:", result)
    print("Leaves evaluated:", nodes_visited, "out of", len(values))
