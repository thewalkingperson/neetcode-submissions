class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for index, value in enumerate(heights):
            start = index
            while stack and stack[-1][1] > value:
                temp = stack.pop()
                area = max(temp[1] * (index - temp[0]), area)
                start = temp[0]
            stack.append([start, value])
        for index, value in stack:
            area = max((len(heights) - index) * value, area)
        
        return area
