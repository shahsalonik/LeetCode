class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, sp in zipped:
            curr = (target - pos) / sp
            if stack and stack[-1] >= curr:
                continue
            else:
                stack.append(curr)
        
        return len(stack)