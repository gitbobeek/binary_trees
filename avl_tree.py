import random


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def height(node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.right) - self.height(node.left)

    def fix_height(self, node):
        hl = self.height(node.left)
        hr = self.height(node.right)
        node.height = max(hl, hr) + 1

    def rotate_right(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root

        self.fix_height(root)
        self.fix_height(new_root)

        return new_root

    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1

    def rotate_left(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root

        self.fix_height(root)
        self.fix_height(new_root)

        return new_root

    def balance(self, node):
        self.fix_height(node)
        if self.balance_factor(node) == 2:
            if self.balance_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if self.balance_factor(node) == -2:
            if self.balance_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return self.balance(root)

    def find_min(self, node):
        return node.left if node.left is None else self.find_min(node.left)

    def find_max(self, node):
        return node.right if node.right is None else self.find_max(node.right)

    def find(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.find(node.left, key)
        else:
            return self.find(node.right, key)

    def remove_min(self, node):
        if node.left is None:
            return node.right
        node.left = self.remove_min(node.left)
        return self.balance(node)

    def remove(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            left = root.left
            right = root.right
            if right is None:
                return left
            min_larger_node = self.find_min(right)
            min_larger_node.right = self.remove_min(right)
            min_larger_node.left = left
            return self.balance(min_larger_node)

        return self.balance(root)

    def fill(self, n):
        generated_keys = set()

        while len(generated_keys) < n:
            key = random.randint(0, n)
            if key not in generated_keys:
                generated_keys.add(key)
                self.root = self.insert(self.root, key)
