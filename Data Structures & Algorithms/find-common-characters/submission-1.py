class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = Counter(words[0])
        holder = None
        for i in words:
            holder = Counter(i)
            for i in temp:
                if i not in holder:
                    temp[i] = 0
                elif temp[i] > holder[i]:
                    temp[i] = holder[i]
        result = []
        for i in temp:
            j = 0
            while j < temp[i]:
                result.append(i)
                j += 1
        
        return result

            

        # temp = set(words[0])
        # holder = set()
        # for i in words[1:]:
        #     for j in i:
        #         if j in temp:
        #             holder.add(j)
        #     temp = holder
        #     holder = set()
        # return list(temp)
            

        