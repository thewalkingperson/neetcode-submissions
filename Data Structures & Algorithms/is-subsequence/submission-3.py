class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        length_of_s = len(s) - 1
        if length_of_s == -1:
            return True

        for right in t:
            if s[left] == right:
                if left == length_of_s:
                    return True
                left += 1
        return False

                
        