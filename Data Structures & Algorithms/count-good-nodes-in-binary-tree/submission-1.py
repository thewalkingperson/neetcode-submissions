# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, max_value):
            if not node:
                return
            
            if node.val >= max_value:
                self.count += 1
                max_value = node.val

            
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        
        dfs(root, root.val)
        return self.count
        # self.count = 0
        # def dfs(node, value):
        #     if not node:
        #         return
        #     if node.value 
        #     self.count += 1
            
        #     if node.left:
        #         if node.left.val <= value:
        #             dfs(node.left, value)
        #     if node.right:
        #         if node.right.val <= value:
        #             dfs(node.right, value)

        # dfs(root, root.val)
        # return self.count


        