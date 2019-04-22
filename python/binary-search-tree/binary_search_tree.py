class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data or None
        self.left = left or None
        self.right = right or None

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
       self.root = None
       create_binary_tree(self, tree_data=tree_data)

    def data(self):
        return recursive_data(self.root)

    def sorted_data(self):
        return inorder_traversal(self.root, None)

def create_binary_tree(self, tree_data):
    self.root = TreeNode(data=tree_data[0], left=None, right=None)
    for data in tree_data[1:]:
        node = TreeNode(data=data, left=None, right=None)
        increment_binary_tree(self, node=node)

def increment_binary_tree(self, node):
    this_node = self.root
    while this_node is not None:
        if node.data <= this_node.data:
            if this_node.left == None:
                this_node.left = node
                return node
            else:
                this_node = this_node.left
        else:
            if this_node.right == None:
                this_node.right = node
                return node
            else:
                this_node = this_node.right
    raise Exception("Traversal went wrong...")       

def recursive_data(node):
    if node is not None:
        recursive_data(node=node.left)
        recursive_data(node=node.right)
    return node

def inorder_traversal(node, sorted_list):
    if sorted_list is None:
        sorted_list = []
    if node is not None:
        inorder_traversal(node.left, sorted_list)
        sorted_list.append(node.data)
        inorder_traversal(node.right, sorted_list)
    return sorted_list