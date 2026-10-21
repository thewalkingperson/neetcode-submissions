class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in helper:
                return [helper[diff],index]
            helper[value] = index

        
        
        