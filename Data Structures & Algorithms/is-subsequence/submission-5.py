class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        length_of_s = len(s)
        if length_of_s == 0:
            return True

        for right in t:
            if s[left] == right:
                left += 1
                if left == length_of_s:
                    return True
        return False

                
        