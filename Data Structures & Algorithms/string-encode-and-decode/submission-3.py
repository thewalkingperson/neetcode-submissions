class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        pointer = 0
        holder = ""
        result = []
        while pointer < len(s):
            if s[pointer] != "#" and s[pointer] in "0123456789":
                holder += s[pointer]
            if s[pointer] == "#":
                temp = pointer + int(holder)
                result.append(s[pointer + 1:temp+1])
                pointer = temp
                holder = ""
            pointer += 1
        return result


