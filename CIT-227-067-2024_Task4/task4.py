# @CIT-227-067/2024 -Danny Ngatia
# %%
# The graph represented as an adjacency dictionary
# Each key is a node, and its value is a list of neighbouring nodes
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
# Defining the start and goal nodes
start = 'A'
goal  = 'G'

# %%
# BFS
from collections import deque

def bfs(graph, start, goal):
    # A queue to hold the paths we are exploring
    # We start with a path containing only the start node
    queue = deque([[start]])

    # A set to keep track of already visited nodes
    visited = set()

    print("=" * 40)
    print("   BREADTH FIRST SEARCH (BFS)")
    print("=" * 40)

    while queue:
        # Take the first path from the front of the queue
        path = queue.popleft()

        # The current node is the last node in the path
        node = path[-1]

        # If we reached the goal, return the path
        if node == goal:
            print(f"\n Goal '{goal}' found!")
            print(f" Path: {' --> '.join(path)}")
            print(f" Total steps: {len(path) - 1}")
            return path

        # If node not yet visited, explore its neighbours
        if node not in visited:
            visited.add(node)

            print(f" Visiting: {node}  |  Queue: {list(queue)}")

            # Add each neighbour as an extended path
            for neighbour in graph[node]:
                new_path = path + [neighbour]
                queue.append(new_path)

    print("No path found.")
    return None

#%%
# DFS
def dfs(graph, start, goal):
    # A stack to hold the paths we are exploring
    # We start with a path containing only the start node
    stack = [[start]]

    # A set to keep track of already visited nodes
    visited = set()

    print("=" * 40)
    print("   DEPTH FIRST SEARCH (DFS)")
    print("=" * 40)

    while stack:
        # Take the last path from the TOP of the stack
        path = stack.pop()

        # The current node is the last node in the path
        node = path[-1]

        # If we reached the goal, return the path
        if node == goal:
            print(f"\n Goal '{goal}' found!")
            print(f" Path: {' --> '.join(path)}")
            print(f" Total steps: {len(path) - 1}")
            return path

        # If node not yet visited, explore its neighbours
        if node not in visited:
            visited.add(node)

            print(f" Visiting: {node}  |  Stack: {list(stack)}")

            # Add neighbours in REVERSE order so left neighbour
            # is explored first (top of stack)
            for neighbour in reversed(graph[node]):
                new_path = path + [neighbour]
                stack.append(new_path)

    print("No path found.")
    return None

# %%

# ── RUN BOTH SEARCHES ─────────────────────────────────
bfs_result = bfs(graph, start, goal)
print()
dfs_result = dfs(graph, start, goal)

# ── COMPARISON SUMMARY ────────────────────────────────
print()
print("=" * 40)
print("        COMPARISON SUMMARY")
print("=" * 40)
print(f"  Start Node     : {start}")
print(f"  Goal Node      : {goal}")
print()
print(f"  BFS Path       : {' --> '.join(bfs_result)}")
print(f"  BFS Steps      : {len(bfs_result) - 1}")
print()
print(f"  DFS Path       : {' --> '.join(dfs_result)}")
print(f"  DFS Steps      : {len(dfs_result) - 1}")
print()
print(f"  Shortest Path  : {'BFS' if len(bfs_result) <= len(dfs_result) else 'DFS'}")
print("=" * 40)