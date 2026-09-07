class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current = 0
        min_length = float("inf")

        for right in range(len(nums)):
            current += nums[right]
            while current >= target:
                min_length = min(min_length, right - left + 1)
                current -= nums[left]
                left += 1

        
        if min_length == float("inf"):
            return 0
        return min_length




        