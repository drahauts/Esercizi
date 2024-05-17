class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def symmetric(tree: list[int]) -> bool:
    def is_symmetric(index_left = 0, index_right = 0):
        if index_left == index_right:
            return True
        if index_right and index_left > len(tree):
            return False
        
        index_middle = len(tree) // 2
        left_tree = tree[:index_middle]
        right_tree = tree[index_middle:]
        print
        pass


tree = [1,2,2,3, 4, 4, 3]
index_middle = len(tree) // 2
left_tree = tree[:index_middle]
right_tree = tree[index_middle:]
print(left_tree, right_tree)