class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+':
                stack.append(stack.pop() + stack.pop())
            elif s == '-':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif s == '*':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 * num1)
            elif s == '/':
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(s))
        return stack[0]