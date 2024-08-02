class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node: TreeNode, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        result = []
        if node:
            result = self._inorder(node.left)
            result.append(node.key)
            result += self._inorder(node.right)
        return result

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        result = []
        if node:
            result.append(node.key)
            result += self._preorder(node.left)
            result += self._preorder(node.right)
        return result

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        result = []
        if node:
            result = self._postorder(node.left)
            result += self._postorder(node.right)
            result.append(node.key)
        return result

    def min_value(self):
        current = self.root
        while current.left:
            current = current.left

        return current.key

    def max_value(self):
        current = self.root
        while current.right:
            current = current.right

        return current.key

    def print_tree_level(self):
        levels = self._get_tree_levels(self.root)
        for i, level in enumerate(levels):
            print("Level", i, ": ", " ".join(str(node) for node in level))

    def _get_tree_levels(self, node, depth=0, levels=None):
        if levels is None:
            levels = []
        if len(levels) == depth:
            levels.append([])

        if node:
            levels[depth].append(node.key)
            self._get_tree_levels(node.left, depth + 1, levels)
            self._get_tree_levels(node.right, depth + 1, levels)

        return levels

    def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root

        print(" " * (level * 4) + prefix + str(node.key))

        if node.left is not None:
            self.print_tree(node.left, level + 1, "L--- ")
        if node.right is not None:
            self.print_tree(node.right, level + 1, "R--- ")

    def sum_nodes(self):
        return self._sum_nodes(self.root)

    def _sum_nodes(self, node):
        if node is None:
            return 0
        return node.key + self._sum_nodes(node.left) + self._sum_nodes(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [15, 10, 20, 8, 12, 16, 25]

    for key in keys:
        bst.insert(key)

    print("In-order traversal:", bst.inorder())
    print("Pre-order traversal:", bst.preorder())
    print("Post-order traversal:", bst.postorder())

    # Searching for a key
    key_to_search = 10
    result = bst.search(key_to_search)
    if result:
        print(f"Key {key_to_search} found in the BST.")
    else:
        print(f"Key {key_to_search} not found in the BST.")

    print("\nTree structure:")
    bst.print_tree_level()
    print("\n")
    bst.print_tree()

    print(f"\nmin value: {bst.min_value()}")
    print(f"max value: {bst.max_value()}")

    print("\nSum of all elements in the tree:", bst.sum_nodes())
