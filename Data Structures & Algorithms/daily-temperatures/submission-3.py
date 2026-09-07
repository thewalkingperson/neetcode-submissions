class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                temp = stack.pop()
                result[temp] = index - temp
            stack.append(index)
        return result