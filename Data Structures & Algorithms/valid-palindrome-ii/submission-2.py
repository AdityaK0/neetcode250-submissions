class Solution:
    def validPalindrome(self, s: str) -> bool:

        valid_range = [ digit for digit in range(48,57+1)]
        valid_range+= [ capital for capital in range(65,90+1)]
        valid_range+= [ small for small in range(95,122+1)]
        

        n = len(s)

        l,r = 0,n-1

        def s_without_given_index(index):

            skip = ""
            for i in range(n):
                if i == index:
                    continue
                skip+=s[i]
            return skip        

        while l<r:

            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                skipL = s_without_given_index(l)
                skipR = s_without_given_index(r)
                return skipL == skipL[::-1] or skipR == skipR[::-1]

        return True        


        

                
                 

        