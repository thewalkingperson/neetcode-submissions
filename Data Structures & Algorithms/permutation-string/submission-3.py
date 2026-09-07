class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = {}
        matches = 0
        set_length = len(set(s1))
        left = 0
        right = 0

        while right < len(s2):
            temp = s2[right]
            if temp in s2_count:
                s2_count[temp] += 1
            else:
                s2_count[temp] = 1
            if temp in s1_count and s2_count[temp] == s1_count[temp]:
                    matches += 1
            if right >= len(s1):
                if s2_count[s2[left]] == s1_count[s2[left]]:
                    matches -= 1
                s2_count[s2[left]] -= 1
                left += 1
            right += 1
            print((left, right))
            if matches == set_length:
                return True
        return False
