N = 8

def is_consistent(assignment, row, col):
"""Check that placing a queen at (row, col) conflicts with no earlier queen.
assignment[r] = column of the queen in row r (rows 0..row-1 are assigned)."""
for r in range(row):
c = assignment[r]
if c == col or abs(c - col) == abs(r - row): # same column or same diagonal
return False
return True

def backtrack(assignment, row, n, stats):
"""Assign one queen per row, trying each column; undo on failure."""
if row == n: # all variables assigned -> solution
return list(assignment)

for col in range(n): # try each value in the domain
stats["tried"] += 1
if is_consistent(assignment, row, col):
assignment[row] = col # assign
result = backtrack(assignment, row + 1, n, stats)
if result is not None:
return result
assignment[row] = -1 # undo (backtrack)
return None # no value works for this row

def solve(n=N):
stats = {"tried": 0}

solution = backtrack([-1] * n, 0, n, stats)
return solution, stats["tried"]

def count_all(assignment, row, n):
"""Enumerate every solution by continuing after each one is found."""
if row == n:
return 1
total = 0
for col in range(n):
if is_consistent(assignment, row, col):
assignment[row] = col
total += count_all(assignment, row + 1, n)
assignment[row] = -1
return total

def show(solution):
n = len(solution)
for r in range(n):
print(" ".join("Q" if solution[r] == c else "." for c in range(n)))
print()

if __name__ == "__main__":
solution, tried = solve()
print("First solution (column of queen in each row):", solution)
print(f"Placements tried: {tried}\n")
show(solution)
print("Total solutions for 8x8:", count_all([-1] * N, 0, N))
