Code:
from collections import deque
def vacuum_cleaner_bfs(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()
    goal_state = ('A', 'Clean', 'Clean')  # Goal: Both rooms should be clean
    while queue:
        (position, room_a, room_b), path = queue.popleft()        
        if (position, room_a, room_b) in visited:
            continue        
        visited.add((position, room_a, room_b))
        path = path + [(position, room_a, room_b)]
        # Check if goal state is reached
        if (room_a, room_b) == ('Clean', 'Clean'):
            return path
        # Possible actions
        actions = []
        if position == 'A':
            if room_a == 'Dirty':
                actions.append(('A', 'Clean', room_b, 'Suck'))  # Clean Room A
            actions.append(('B', room_a, room_b, 'Move to B'))  # Move to Room B
        elif position == 'B':
            if room_b == 'Dirty':
                actions.append(('B', room_a, 'Clean', 'Suck'))  # Clean Room B
            actions.append(('A', room_a, room_b, 'Move to A'))  # Move to Room A
        # Expand the search tree
        for new_position, new_room_a, new_room_b, action in actions:
            queue.append(((new_position, new_room_a, new_room_b), path + [(action, new_position, new_room_a, new_room_b)]))    
    return None  # No solution found
# Input from user
room_a = input("Enter Room A status (Clean/Dirty): ").strip()
room_b = input("Enter Room B status (Clean/Dirty): ").strip()
vacuum_position = input("Enter Vacuum position (A/B): ").strip()
# Run BFS solver
solution = vacuum_cleaner_bfs((vacuum_position, room_a, room_b))
# Print solution
if solution:
    print("Solution found:")
    for step, state in enumerate(solution):
        if len(state) == 3:
            print(f"Step {step}: Vacuum in {state[0]}, Room A: {state[1]}, Room B: {state[2]}")
        else:
            print(f"Step {step}: Action: {state[0]}, Vacuum in {state[1]}, Room A: {state[2]}, Room B: {state[3]}")
else:
    print("No solution found.")
Output:
Enter Room A status (Clean/Dirty): Dirty
Enter Room B status (Clean/Dirty): Dirty
Enter Vacuum position (A/B): A
Solution found:
Step 0: Vacuum in A, Room A: Dirty, Room B: Dirty
Step 1: Action: Suck, Vacuum in A, Room A: Clean, Room B: Dirty
Step 2: Vacuum in A, Room A: Clean, Room B: Dirty
Step 3: Action: Move to B, Vacuum in B, Room A: Clean, Room B: Dirty
Step 4: Vacuum in B, Room A: Clean, Room B: Dirty
Step 5: Action: Suck, Vacuum in B, Room A: Clean, Room B: Clean
Step 6: Vacuum in B, Room A: Clean, Room B: Clean
