# Binary Search Tree (BST) Implementation in Python

This repository contains a simple and clear implementation of a Binary Search Tree (BST) in Python. It supports insertion, search, deletion, and different tree traversals (inorder, preorder, postorder).

---

## Features

- Insert nodes into the BST
- Search for a key in the BST
- Delete nodes from the BST (handles all cases: no child, one child, two children)
- Traverse the tree in inorder, preorder, and postorder

---

## Code Overview

The BST is implemented using two classes:

- `Node`: Represents a node in the BST.
- `BST`: Contains methods to manipulate the BST, including insertion, deletion, searching, and traversals.

---

## Usage Example

```python
if __name__ == "__main__":
    bst = BST()

    # Insert values into the BST
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Inorder (sorted):", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())

    # Search for a key
    key = 40
    print(f"Search {key}:", "Found" if bst.search(key) else "Not Found")

    # Delete a node
    bst.delete(30)
    print("After deleting 30, inorder:", bst.inorder())

