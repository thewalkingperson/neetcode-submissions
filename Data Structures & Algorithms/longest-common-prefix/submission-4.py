class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        length = len(prefix)

        for i in strs:
            i_length = len(i) - 1
            for index in range(0, length):
                
                if i_length < index or prefix[index] != i[index]:
                    length = index
                    break
        
        return strs[0][0:length]

