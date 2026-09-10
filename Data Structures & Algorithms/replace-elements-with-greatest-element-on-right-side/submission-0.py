class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        greatest = arr[-1]
        index = len(arr) - 1

        while index >= 0:
            temp = arr[index]
            arr[index] = greatest
            greatest = max(temp, greatest)
            index -= 1
        
        arr[-1] = -1

        return arr

            

        