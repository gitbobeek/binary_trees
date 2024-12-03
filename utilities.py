def print_tree(node, space=0, height=10):
    if node is None:
        return

    space += height

    print_tree(node.right, space)

    print()
    for i in range(height, space):
        print(" ", end="")
    print(node.key)

    print_tree(node.left, space)

def find(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return find(node.left, key)
    else:
        return find(node.right, key)

