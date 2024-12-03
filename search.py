from collections import deque


def bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.key)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


def preorder_traversal(node):
    if node is not None:
        print(node.key, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=" ")


def traverse(root, order='inorder'):
    if order == 'preorder':
        print("Обход в прямом порядке (pre-order):")
        preorder_traversal(root)
    elif order == 'inorder':
        print("Симметричный обход (in-order):")
        inorder_traversal(root)
    elif order == 'postorder':
        print("Обратный обход (post-order):")
        postorder_traversal(root)
    else:
        print("Неподдерживаемый режим обхода.")