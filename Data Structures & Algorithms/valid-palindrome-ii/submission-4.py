class Solution:
    def validPalindrome(self, s: str) -> bool:



        l,r = 0,len(s)-1

        def isPalindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1

            return True        

        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return isPalindrome(l+1,r) or isPalindrome(l,r-1)    
        
        return True


        #TC and SC both is 0(n)2
        # valid_range = [ digit for digit in range(48,57+1)]
        # valid_range+= [ capital for capital in range(65,90+1)]
        # valid_range+= [ small for small in range(97,122+1)]
        

        # n = len(s)

        # l,r = 0,n-1

        # def s_without_given_index(index):

        #     skip = ""
        #     for i in range(n):
        #         if i == index:
        #             continue
        #         skip+=s[i]
        #     return skip        

        # while l<r:

        #     if s[l] == s[r]:
        #         l+=1
        #         r-=1
        #     elif ord(s[l]) not in valid_range:
        #         l+=1
        #     elif ord(s[r]) not in valid_range:  
        #         r-=1     
        #     else:
        #         skipL = s_without_given_index(l)
        #         skipR = s_without_given_index(r)
        #         return skipL == skipL[::-1] or skipR == skipR[::-1]

        # return True        


        

                
                 

        