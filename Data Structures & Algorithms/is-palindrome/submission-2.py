class Solution:

    def is_alpha(self,keys):
        return ord('A') <= ord(keys) <= ord('Z') or ord('a') <= ord(keys) <= ord('z') or ord('0') <= ord(keys) <= ord('9')


    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) - 1

        while l < r:

            while l < r and not self.is_alpha(s[l]):
                l += 1
            while l < r and not self.is_alpha(s[r]):
                r -= 1                

            if s[l].lower() != s[r].lower():
                return False
            else:
                l,r = l+1,r-1
        return True
            

    
        