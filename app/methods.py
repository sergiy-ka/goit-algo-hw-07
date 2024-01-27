from app.node import Node


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current.val


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current.val


def sum_values(root):
    if root is None:
        return 0
    return sum_values(root.left) + root.val + sum_values(root.right)
