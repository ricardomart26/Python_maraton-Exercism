class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)
    
    def lr(self, data):
        if data <= self.data:
            if self.left:
                self.left.lr(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.lr(data)
            else:
                self.right = TreeNode(data)                
    
    def sorted(self, list):
        if self.left:
            self.left.sorted(list)
        list.append(self.data)
        if self.right:
            self.right.sorted(list)
        return list

class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        tree_data.pop(0)
        for x in tree_data:
            self.root.lr(x)
    
    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.sorted([])
