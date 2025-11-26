class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr = 1
                curr_num = num
                while curr_num + 1 in num_set:
                    curr += 1
                    curr_num += 1
                if curr > longest:
                    longest = curr

        return longest