class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        #48-57 65-90 97-122
        num_range = [ number for number in range(48,57+1) ]
        small_alpha_range = [ char for char in range(97,122+1)]
        capital_alpha_range = [ char for char in range(65,90+1)]

        valid_range = num_range + capital_alpha_range + small_alpha_range

        while l<r:
            if s[l]==" " or ord(s[l]) not in valid_range:
                l+=1
            elif s[r]==" " or ord(s[r]) not in valid_range:
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1 
            else:
                return False

        return True                       

