class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_dict = Counter(t)
        for i in s:
            if i not in t_dict or t_dict[i] <= 0:
                return False
            t_dict[i] -= 1
        
        return True

            