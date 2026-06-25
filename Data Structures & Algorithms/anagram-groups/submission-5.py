class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        res = defaultdict(list)
        
        for i in strs:
            sorted_keys = ''.join(sorted(i))
            res[sorted_keys].append(i)
        return list(res.values())
        