# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, left, right):
            if not root:
                return True
            if not left < root.val or not right > root.val:
                return False
            
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)


        return valid(root, float('-inf'), float('inf'))


        
        # if not root:
        #     return True
        # queue = deque()
        # queue.append(root)

        # while queue:
        #     for i in range(len(queue)):
        #         temp = queue.popleft()
        #         if temp.left:
        #             if temp.left.val < temp.val:
        #                 queue.append(temp.left)
        #             else:
        #                 return False
                
        #         if temp.right:
        #             if temp.right.val > temp.val:
        #                 queue.append(temp.right)
        #             else:
        #                 return False
        return True

        

        