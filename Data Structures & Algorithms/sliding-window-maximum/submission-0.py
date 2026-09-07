from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        right = 0
        output = []

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if right + 1 >= k:
                output.append(nums[queue[0]])
                if queue[0] <= left:
                    queue.popleft()
                left += 1
            right += 1
        
        return output


        