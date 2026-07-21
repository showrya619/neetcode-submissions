class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i,n in enumerate(nums):

            needed = target - n

            if needed in hashmap:
                return [hashmap[needed],i]
            else:
                hashmap[n]=i
        return False
        