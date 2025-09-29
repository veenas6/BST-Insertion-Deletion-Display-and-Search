class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---------- Insertion ----------
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # Ignore duplicates
        return node

    # ---------- Search ----------
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # ---------- Deletion ----------
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:  # Found the node to delete
            # Case 1: No child
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Two children
            temp = self._minValueNode(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # ---------- Traversals ----------
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.key] + self._inorder(node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.key] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.key]


# ---------- Example Usage ----------
if __name__ == "__main__":
    bst = BST()

    # Insert values into the BST
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Inorder (sorted):", bst.inorder())
    print("Preorder:", bst.preorder())
    print("Postorder:", bst.postorder())

    # Search
    key = 40
    print(f"Search {key}:", "Found" if bst.search(key) else "Not Found")

    # Delete a node
    bst.delete(30)
    print("After deleting 30, inorder:", bst.inorder())