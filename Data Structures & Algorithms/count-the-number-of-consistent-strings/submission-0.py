class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        holder = set(allowed)
        count = 0
        for i in words:
            length_count = 0
            for j in i:
                if j not in holder:
                    break
                else:
                    length_count += 1
            if length_count == len(i):
                count += 1
            
        return count

        