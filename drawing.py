def draw_tree(node, prefix="", is_left=True):
    if node is not None:
        result = prefix + ("├── " if is_left else "└── ") + str(node.key) + "\n"
        next_prefix = prefix + ("│   " if is_left else "    ")
        result += draw_tree(node.left, next_prefix, True)
        result += draw_tree(node.right, next_prefix, False)
        return result
    return ""