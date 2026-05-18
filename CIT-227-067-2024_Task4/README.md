@CIT-227-067/2024 -DAnny Ngatia
# Task 4: Breadth-First Search (BFS) vs Depth-First Search (DFS)

## Overview
This task implements and compares two fundamental graph traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**. Both algorithms search for a path from a start node to a goal node in a directed graph.

## Graph Structure
The task uses the following directed graph represented as an adjacency dictionary:

```
    A
   / \
  B   C
 / \   \
D   E   F
    |
    G
```

**Graph Definition:**
- A → B, C
- B → D, E
- C → F
- D → (no neighbors)
- E → G
- F → (no neighbors)
- G → (no neighbors)

**Search Task:** Find a path from node `A` (start) to node `G` (goal)

## Algorithms

### Breadth-First Search (BFS)
- **Data Structure:** Queue (FIFO - First In, First Out)
- **Approach:** Explores all neighbors of the current node before moving deeper
- **Characteristics:**
  - Finds the **shortest path** (in terms of number of steps)
  - More memory intensive for large graphs
  - Better for finding shortest distances
- **Expected Path:** A → B → E → G (3 steps)

### Depth-First Search (DFS)
- **Data Structure:** Stack (LIFO - Last In, First Out)
- **Approach:** Explores as far as possible along each branch before backtracking
- **Characteristics:**
  - Does not guarantee the shortest path
  - More memory efficient than BFS
  - Better for exploring all possible solutions
  - Neighbors are added in reverse order to maintain left-to-right exploration
- **Expected Path:** A → B → E → G (3 steps) or A → B → D (2 steps if D is goal)

## Running the Code

### Prerequisites
- Python 3.x installed
- No external dependencies required (uses only built-in `collections.deque`)

### Execution
Run the script in a Python environment:
```bash
python task4.py
```

## Output
The script produces three sections of output:

1. **BFS Output** - Shows each node visited, the queue state, and the final path found
2. **DFS Output** - Shows each node visited, the stack state, and the final path found
3. **Comparison Summary** - Displays:
   - Start and goal nodes
   - BFS path and step count
   - DFS path and step count
   - Which algorithm found the shortest path

### Example Output
```
========================================
   BREADTH FIRST SEARCH (BFS)
========================================
 Visiting: A  |  Queue: [['B'], ['C']]
 Visiting: B  |  Queue: [['C'], ['D'], ['E']]
 Visiting: C  |  Queue: [['D'], ['E'], ['F']]
 Visiting: D  |  Queue: [['E'], ['F']]
 Visiting: E  |  Queue: [['F'], ['G']]

 Goal 'G' found!
 Path: A --> B --> E --> G
 Total steps: 3
```

## Key Concepts

| Aspect | BFS | DFS |
|--------|-----|-----|
| **Data Structure** | Queue | Stack |
| **Order** | Level-by-level | Branch-by-branch |
| **Shortest Path** | ✓ Guaranteed | ✗ Not guaranteed |
| **Space Complexity** | O(w) - width of graph | O(h) - height of graph |
| **Time Complexity** | O(V + E) | O(V + E) |
| **Best Use Case** | Shortest path problems | Topological sorting, cycle detection |

## Implementation Notes

1. **Visited Set:** Both algorithms use a `visited` set to avoid revisiting nodes
2. **Path Tracking:** Paths are stored as lists that grow as we explore neighbors
3. **Reverse Order in DFS:** Neighbors are processed in reverse order in DFS to ensure left-to-right exploration when using a stack (which processes elements in LIFO order)

## Learning Outcomes
- Understanding how BFS and DFS traverse graphs differently
- Recognizing when to use each algorithm based on problem requirements
- Implementing queue-based and stack-based search strategies
- Analyzing algorithm efficiency and correctness

## Modifications & Extensions
To experiment with this code:
- Change the `graph` dictionary to test with different graph structures
- Modify `start` and `goal` variables to search between different nodes
- Add heuristics to implement A* or best-first search
- Implement path visualization
