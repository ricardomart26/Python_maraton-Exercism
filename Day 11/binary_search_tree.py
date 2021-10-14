class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree_data = tree_data

    def data(self):
        size = len(self.tree_data)
        if size == 1:
            return TreeNode(self.tree_data[0])
        
    def sorted_data(self):
        return self.tree_data.sort()
