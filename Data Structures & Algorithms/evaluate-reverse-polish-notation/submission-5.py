class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                temp = int(stack.pop())
                stack.append(int(stack.pop()) - temp)
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                temp = int(stack.pop())
                stack.append(int(stack.pop())/temp)
            else:
                stack.append(int(i))
            print(stack)
        return int(stack[0])
        