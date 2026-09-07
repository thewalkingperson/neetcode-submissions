class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        index = 0
        if left == right:
            return index
        while index < len(nums):
            left += nums[index]
            if left == right:
                return index
            print(left)
            print(right)
            right -= nums[index]
            index += 1
        return -1
        