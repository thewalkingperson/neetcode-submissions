# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            value = []
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                value.append(temp.val)
            result.append(value[len(value) - 1])
        return result
        # result.append(root.val)
        # while root.right:
        #     result.append(root.right.val)
        #     root = root.right
        # return result


            



