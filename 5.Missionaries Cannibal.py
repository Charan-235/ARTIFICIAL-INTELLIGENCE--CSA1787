Code:
from collections import deque
# Define the possible moves (Missionaries, Cannibals)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
def is_valid(state):
    """Check if a given state is valid (no more cannibals than missionaries on either side)."""
    left_m, left_c, _, right_m, right_c = state
    return (left_m == 0 or left_m >= left_c) and (right_m == 0 or right_m >= right_c)
def generate_next_states(state):
    """Generate all possible next valid states."""
    left_m, left_c, boat, right_m, right_c = state
    next_states = []    
    if boat == 1:  # Boat on the left side
        for m, c in moves:
            if left_m >= m and left_c >= c:  # Ensure we have enough missionaries & cannibals
                new_state = (left_m - m, left_c - c, 0, right_m + m, right_c + c)
                if is_valid(new_state):
                    next_states.append(new_state)
    else:  # Boat on the right side
        for m, c in moves:
            if right_m >= m and right_c >= c:
                new_state = (left_m + m, left_c + c, 1, right_m - m, right_c - c)
                if is_valid(new_state):
                    next_states.append(new_state)    
    return next_states
def bfs():
    """Perform BFS to find the solution."""
    initial_state = (3, 3, 1, 0, 0)  # (Left missionaries, Left cannibals, Boat side, Right missionaries, Right cannibals)
    goal_state = (0, 0, 0, 3, 3)  # All moved to the right    
    queue = deque([(initial_state, [])])  # (Current state, Path taken)
    visited = set()    
    while queue:
        current_state, path = queue.popleft()        
        if current_state in visited:
            continue
        visited.add(current_state)       
        new_path = path + [current_state]        
        if current_state == goal_state:
            return new_path  # Solution found        
        for next_state in generate_next_states(current_state):
            queue.append((next_state, new_path))    
    return None  # No solution found
# Solve the problem
solution = bfs()
# Print the solution
if solution:
    print("Solution found in", len(solution) - 1, "moves:")
    for step, state in enumerate(solution):
        left_m, left_c, boat, right_m, right_c = state
        boat_side = "Left" if boat == 1 else "Right"
        print(f"Step {step}: Left({left_m}M, {left_c}C) | Boat({boat_side}) | Right({right_m}M, {right_c}C)")
else:
    print("No solution found.")
Output:
Solution found in 11 moves:
Step 0: Left(3M, 3C) | Boat(Left) | Right(0M, 0C)
Step 1: Left(3M, 1C) | Boat(Right) | Right(0M, 2C)
Step 2: Left(3M, 2C) | Boat(Left) | Right(0M, 1C)
Step 3: Left(3M, 0C) | Boat(Right) | Right(0M, 3C)
Step 4: Left(3M, 1C) | Boat(Left) | Right(0M, 2C)
Step 5: Left(1M, 1C) | Boat(Right) | Right(2M, 2C)
Step 6: Left(2M, 2C) | Boat(Left) | Right(1M, 1C)
Step 7: Left(0M, 2C) | Boat(Right) | Right(3M, 1C)
Step 8: Left(0M, 3C) | Boat(Left) | Right(3M, 0C)
Step 9: Left(0M, 1C) | Boat(Right) | Right(3M, 2C)
Step 10: Left(1M, 1C) | Boat(Left) | Right(2M, 2C)
Step 11: Left(0M, 0C) | Boat(Right) | Right(3M, 3C)
