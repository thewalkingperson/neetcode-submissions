class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                i = stack.pop()
                result[i] = index - i
            stack.append(index)
        return result

                