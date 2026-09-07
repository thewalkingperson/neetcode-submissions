# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0]) #first value of preorder is the root
        mid = inorder.index(preorder[0]) #finds index in inorder of the root
        
        #skip zero index since it is root and plus one to include mid since its exclusive  
        #inorder takes start to just before mid      
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) 

        
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root




        # dummy = Listnode()
        # curr = dummy
        # dummy.val = preorder[0]
        # i = 1
        # if inorder[0] != preorder[0]:
        #     curr.left = ListNode(inorder[0], None)
        #     curr = curr.left
        # i = 1
        # while i < len(inorder) and inorder[i] != preorder[0]:
        #     curr.left = Listnode(inorder[i], None)
        #     i += 1
        #     if i < len(inorder) and inorder[i] != preorder[0]:
        #         curr.right = Listnode(inorder[i], None)
        #         i += 1
        
        

