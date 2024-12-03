import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)


    def insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        else:
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_larger_node = self.find_min(node.right)
            node.key = min_larger_node.key
            node.right = self.delete_recursive(node.right, min_larger_node.key)
        return node

    @staticmethod
    def find_min(node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def get_height(self, node):
        if node is None:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1

    def fill(self, n):
        generated_keys = set()

        while len(generated_keys) < n:
            key = random.randint(0, n)
            if key not in generated_keys:
                generated_keys.add(key)
                self.insert(key)

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            self.print_tree(node.right, level + 1, "R----")
            print(" " * (level * 6) + prefix + str(node.key))
            self.print_tree(node.left, level + 1, "L----")