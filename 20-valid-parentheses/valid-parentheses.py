class Solution:
    def isValid(self, s: str) -> bool:
        hp = {')': '(', '}': '{', ']': '['} 
        stack = []

        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                stack.append(letter)
            else:
                if len(stack) > 0 and stack[-1] == hp[letter]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0