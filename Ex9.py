class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def in_order_traversal(node):
    if node is None:
        return []
    return (
        in_order_traversal(node.left) +
        [node.value] +
        in_order_traversal(node.right)
    )