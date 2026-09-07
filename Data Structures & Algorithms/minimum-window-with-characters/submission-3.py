class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        current_count = 0
        current = {}
        t_count = 0
        t_hashmap = {}
        result = (0, len(s) + 1)

        for i in t:
            if i in t_hashmap:
                t_hashmap[i] += 1
            else:
                t_hashmap[i] = 1
                t_count += 1

        while right < len(s):
            if s[right] in current:
                current[s[right]] += 1
            else:
                current[s[right]] = 1
            if s[right] in t_hashmap and current[s[right]] == t_hashmap[s[right]]:
                current_count += 1
            while current_count == t_count:
                if right - left < result[1] - result[0]:
                    result = (left, right)
                current[s[left]] -= 1
                if s[left] in t_hashmap and current[s[left]] + 1 == t_hashmap[s[left]]:
                    current_count -= 1
                left += 1
            right += 1
        print(result)
        
        if result[1] < len(s) + 1:
            return s[result[0]:result[1] + 1]
        return ""
        


            


         




        