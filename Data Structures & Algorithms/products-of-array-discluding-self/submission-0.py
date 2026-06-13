class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,n in enumerate(nums):
            nums.pop(i)
            res.append(math.prod(nums))
            nums.insert(i,n)
        return res