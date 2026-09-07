class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = len(digits) - 1
        while temp >= 0:
            if digits[temp] == 9:
                digits[temp] = 0
                temp -= 1
            else:
                digits[temp] += 1
                break
        if digits[0] == 0:
            return [1] + digits
        return digits

                
