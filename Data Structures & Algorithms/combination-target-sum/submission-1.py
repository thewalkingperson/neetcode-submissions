class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        n = len(nums)

        def dfs(index, value):
            if value == target:
                result.append(subset[:])
                return
            if value > target or index == n:
                return
            
            dfs(index+1, value)

            subset.append(nums[index])

            dfs(index, value + nums[index])
            subset.pop()

        dfs(0,0)
        return result
