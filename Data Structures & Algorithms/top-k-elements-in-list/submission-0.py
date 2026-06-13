class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        return sorted(hashmap,key=lambda x: hashmap[x], reverse=True)[:k]
                