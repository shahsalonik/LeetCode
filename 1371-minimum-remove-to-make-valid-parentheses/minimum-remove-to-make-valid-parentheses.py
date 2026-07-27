class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = ""
        ignore_set = set()
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop() 
                else:
                    ignore_set.add(i)

        while stack:
            elem = stack.pop()
            ignore_set.add(elem)
        
        for i, c in enumerate(s):
            if i in ignore_set:
                continue    
            res += c

        return res