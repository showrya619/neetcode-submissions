class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}

        for i,n in enumerate(nums):
            needed = target - n

            if needed in prevmap:
                return [prevmap[needed],i]
            else:
                prevmap[n] = i
        return False
        