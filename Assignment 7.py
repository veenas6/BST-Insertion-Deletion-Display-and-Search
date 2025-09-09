#Asssignment 1: BFS and DFS

# Group D Assignment 1: BFS & DFS
from collections import deque

# Mapping location names to indices for matrix representation
locations = ['A', 'B', 'C', 'D']
location_index = {name: idx for idx, name in enumerate(locations)}

# ------------------------------
# DFS using Adjacency Matrix
# ------------------------------

# Graph represented as adjacency matrix
adj_matrix = [
    # A  B  C  D
    [ 0, 1, 1, 0],  # A
    [ 1, 0, 0, 1],  # B
    [ 1, 0, 0, 1],  # C
    [ 0, 1, 1, 0]   # D
]

def dfs_matrix(start):
    visited = [False] * len(locations)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(locations[node])
        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    dfs(location_index[start])
    return result

# ------------------------------
# BFS using Adjacency List
# ------------------------------

# Graph represented as adjacency list
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

# ------------------------------
# Run the algorithms
# ------------------------------
def menu():
    print("\n===== Menu =====")
    print("1. DFS")
    print("2. BFS")
    print("3. Exit")

while True:
  menu()
  choice = input("Enter your choice: ")

  if choice == '1':
    start_location = 'A'
    dfs_result = dfs_matrix(start_location)
    print("DFS Traversal (using adjacency matrix):", dfs_result)

  if choice == '2':
    start_location = 'A'
    bfs_result = bfs_list(start_location)
    print("BFS Traversal (using adjacency list):", bfs_result)

  if choice == '3':
    break



