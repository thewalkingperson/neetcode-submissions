class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for word in words:
            temp = Counter(chars)
            subtotal = 0
            for char in word:
                if char not in temp or temp[char] == 0:
                    break
                else:
                    temp[char] -= 1
                    subtotal += 1
            if subtotal == len(word):
                total += subtotal
        return total
            


        