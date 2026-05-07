"""
SearchTrees.py
Starter version for CSC 223 Course Schedule Trees Project

This file provides:
- BSTMap: Binary Search Tree Map (unbalanced)
- AVLTreeMap: Self-balancing AVL Tree Map

*** Height methods have been intentionally removed. ***
Students must implement height() for BOTH trees.

Do NOT modify insertion, rotation, search, or node classes.
Only implement the height() functions where marked TODO.
"""

# ---------------------------------------------------------
# ---------------  BINARY SEARCH TREE (BST) ---------------
# ---------------------------------------------------------

class _BSTNode:
    __slots__ = "key", "value", "left", "right"

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTMap:
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        self._root = self._insert_recursive(self._root, key, value)

    def _insert_recursive(self, node, key, value):
        if node is None:
            return _BSTNode(key, value)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            node.value = value
        return node

    def search(self, key):
        return self._search_recursive(self._root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search_recursive(node.left, key)
        elif key > node.key:
            return self._search_recursive(node.right, key)
        return node.value

    def inorder_items(self):
        yield from self._inorder_recursive(self._root)

    def _inorder_recursive(self, node):
        if node:
            yield from self._inorder_recursive(node.left)
            yield (node.key, node.value)
            yield from self._inorder_recursive(node.right)

    # REQUIRED FOR PROJECT
    def height(self):
        def _h(node):
            if node is None:
                return -1
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self._root)


# ---------------------------------------------------------
# ---------------------- AVL TREE MAP ---------------------
# ---------------------------------------------------------

class _AVLNode:
    __slots__ = "key", "value", "left", "right", "height"

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTreeMap:
    def __init__(self):
        self._root = None

    def insert(self, key, value):
        self._root = self._insert_recursive(self._root, key, value)

    def _insert_recursive(self, node, key, value):
        if node is None:
            return _AVLNode(key, value)

        if key < node.key:
            node.left = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, value)
        else:
            node.value = value
            return node

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def search(self, key):
        return self._search_recursive(self._root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            return self._search_recursive(node.left, key)
        elif key > node.key:
            return self._search_recursive(node.right, key)
        return node.value

    def inorder_items(self):
        yield from self._inorder_recursive(self._root)

    def _inorder_recursive(self, node):
        if node:
            yield from self._inorder_recursive(node.left)
            yield (node.key, node.value)
            yield from self._inorder_recursive(node.right)

    def _get_height(self, node):
        return node.height if node else -1

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    # REQUIRED FOR PROJECT
    def height(self):
        def _h(node):
            if node is None:
                return -1
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self._root)
