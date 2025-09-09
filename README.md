## Overview

This Python program demonstrates the implementation of **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** algorithms on a graph with four locations: A, B, C, and D.

- **DFS** uses an adjacency matrix representation.
- **BFS** uses an adjacency list representation.
- The program provides an interactive menu to choose the traversal method starting from node 'A'.

## Features

- DFS traversal using recursion and adjacency matrix.
- BFS traversal using a queue and adjacency list.
- Interactive menu for selecting traversal type.
- Clear display of traversal order.

## Graph Representation

**Adjacency Matrix (for DFS):**

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 |
| B | 1 | 0 | 0 | 1 |
| C | 1 | 0 | 0 | 1 |
| D | 0 | 1 | 1 | 0 |

**Adjacency List (for BFS):**

```python
{
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D'],
  'D': ['B', 'C']
}
'''

## Technologies Used
- **Python 3** — Programming language used for implementing the algorithms.  
- **collections.deque** — Python’s built-in double-ended queue used to efficiently implement the BFS queue.  
- **Recursion** — Used in DFS implementation for traversing the graph.  
- **Data Structures** — Adjacency matrix and adjacency list representations of graphs.


