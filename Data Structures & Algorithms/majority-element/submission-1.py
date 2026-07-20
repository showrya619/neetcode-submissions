class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        return max(count,key=count.get)