class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for letters in zip(*strs):
            print(letters)
            if len(set(letters)) == 1:
                res += letters[0]
            else:
                break   
        return res    
        