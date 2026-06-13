class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)

        for keys in strs:
            sorted_keys = ''.join(sorted(keys))
            res[sorted_keys].append(keys)
        return list(res.values())