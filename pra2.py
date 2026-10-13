
grid = [
    ['S', '.', '#', '.'],
    ['.', '.', '#', '.'],
    ['#', '.', '.', '.'],
    ['.', '#', '.', 'G']
]

# Initial position of the agent
position = (0, 0)

# Internal state of the agent
internal_state = {}

# Possible movements
moves = {
    "Up": (-1, 0),
    "Down": (1, 0),
    "Left": (0, -1),
    "Right": (0, 1)
}

# Function to perceive the current cell
def perceive(position):
    row, col = position
    return grid[row][col]

# Function to update internal state
def update_state(position):
    row, col = position
    internal_state[position] = grid[row][col]

# Function to choose the next action
def choose_action(position):
    row, col = position

    # Prefer unvisited cells
    for action, (dr, dc) in moves.items():
        new_row = row + dr
        new_col = col + dc

        # Check boundaries
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # Check if cell is free or goal
            if grid[new_row][new_col] in ['.', 'G']:
                if (new_row, new_col) not in internal_state:
                    return action

    # If no unvisited cell is available, allow any valid movement
    for action, (dr, dc) in moves.items():
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] in ['.', 'G']:
                return action

    return "No valid move"


# Display initial grid
print("Initial Grid:")
for row in grid:
    print(row)

print("\nAgent starts at:", position)

# Agent loop
for i in range(20):
    # Perceive environment
    percept = perceive(position)

    # Update internal state
    update_state(position)

    print("\nStep:", i + 1)
    print("Current Position:", position)
    print("Percept:", percept)
    print("Internal State:", internal_state)

    # Check whether goal is reached
    if percept == 'G':
        print("Goal Reached!")
        break

    # Choose action
    action = choose_action(position)
    print("Action:", action)

    if action == "No valid move":
        print("Agent is stuck!")
        break

    # Perform action
    dr, dc = moves[action]
    position = (position[0] + dr, position[1] + dc)
