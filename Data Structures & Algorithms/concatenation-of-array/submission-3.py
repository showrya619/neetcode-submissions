class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lens = len(nums)
        ans = [0] * (2*lens)
        for i,n in enumerate(nums):
            ans[i] = ans[i+lens] = n
        return ans