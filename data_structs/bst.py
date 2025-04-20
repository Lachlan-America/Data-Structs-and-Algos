class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        # In the case that the root node doesn't exist
        if not self.root:
            self.root = TreeNode(value)
        else:
            # Recursively insert the value into the tree
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int) -> None:
        # If the value is less than the current node's value, go left
        # If the value is greater than the current node's value, go right
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        # Initial conditions for the search
        if not self.root:
            return None
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: TreeNode, value: int):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)