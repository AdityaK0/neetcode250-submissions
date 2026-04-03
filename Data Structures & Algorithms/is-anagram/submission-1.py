class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        return s==t




        # catch is that it will run if no need to check by each character
        # so the length should be also same in another string 

        # t_set = set(t)
        # for ch in s:
        #     if ch not in t_set: # direct find in array gonna take 0(n) TC for each element
        #                     # so converted that into set which will take only 0(1)
        #         return False
        # return True        
        