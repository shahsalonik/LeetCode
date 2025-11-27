class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # while the temp is greater than the last elem pushed onto stack
            # pop, and set the result info
            # stack_ind stores the index in the list
            while stack and temp > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                result[stack_ind] = i - stack_ind
            stack.append((temp, i))
        
        return result