class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # pair of elements(index, heights)

        for index, value in enumerate(heights):
            start = index
            while stack and stack[-1][1] > value:
                temp = stack.pop()
                area = max((index-temp[0]) * temp[1], area)
                start = temp[0]
            stack.append((start, value))
        
        for index, value in stack:
            area = max((len(heights)-index) * value, area)
        return area