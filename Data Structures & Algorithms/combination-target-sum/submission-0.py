class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        n = len(nums)

        def dfs(i, cur_sum):
            if cur_sum == target:
                result.append(subset[:])
                return
            if cur_sum > target or i == n:
                return
        
            dfs(i + 1, cur_sum)

            subset.append(nums[i])
            dfs(i, cur_sum + nums[i])
            subset.pop()

        dfs(0,0)
        return result
