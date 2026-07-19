class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        for char in nums:
            count[char] = 1 + count.get(char,0) 

        return max(count,key=count.get)            

        