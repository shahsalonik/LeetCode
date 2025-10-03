class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            anagram_map[sortedS].append(s)

        return list(anagram_map.values())