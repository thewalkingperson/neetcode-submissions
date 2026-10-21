from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1

            dictionary[tuple(count)].append(word)
        return list(dictionary.values())
        
        
        