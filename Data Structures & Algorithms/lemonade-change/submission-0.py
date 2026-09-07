class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0,0,0]
        for bill in bills:
            if bill == 5:
                arr[0] += 1
            elif bill == 10:
                if arr[0] == 0:
                    return False
                arr[0] -= 1
                arr[1] += 1
            elif bill == 20:
                if (arr[1] < 1 or arr[0] < 1) and arr[0] < 3:
                    return False
                if arr[1] > 0:
                    arr[1] -= 1
                    arr[0] -= 1
                    arr[2] += 1
                else:
                    arr[0] -= 3
                    arr[2] += 1
        return True
        