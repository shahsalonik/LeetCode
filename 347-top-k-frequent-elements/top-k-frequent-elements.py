class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_items_desc = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        result = []

        for elem in sorted_items_desc:
            if len(result) >= k:
                break
            result.append(elem[0])

        return result