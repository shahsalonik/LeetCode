class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        nums_dict = Counter(nums)
        result = []
        # this is how you sort a dictionary in python in descending order
        output = dict(sorted(nums_dict.items(), key=lambda item: item[1], reverse=True))
        key_list = list(output.keys())
        while len(result) < k:
            result.append(key_list[len(result)])
        return result