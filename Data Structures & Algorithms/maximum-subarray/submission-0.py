class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        max_count = float('-inf')
        for i in nums:
            count += i
            max_count = max(count, max_count)

            if count < 0:
                count = 0
        
        return max_count


        