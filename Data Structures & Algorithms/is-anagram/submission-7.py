class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # best optimal way is using array hashing

        count = [0]*26

        for i in range(len(s)):
            count[ord(s[i]) - ord("a")]+=1
            count[ord(t[i]) - ord("a")]-=1

        return all(ctn==0 for ctn in count)    

        # s_hash_map = {}
    
        # best way is can be like this but taken o(n) space 
        
        # for ch in s:
        #     s_hash_map[ch] = s_hash_map.get(ch,0)+1
        
        # for ch in t:
        #     s_hash_map[ch] = s_hash_map.get(ch,0)-1  
            
        # for key in s_hash_map.values():
        #     if key!=0:
        #         return False
        
        # return True     
                     

        #way2 
        # make t as a list and start remove each element which s have if character not found means False 
        # if len(t)!=len(s):
        #     return False
        # a = list(t)
        # for i in s:
        #     try:
        #         a.remove(i)
        #     except:
        #         return False

        # return True                

        # way1 
        # s=sorted(s)
        # t=sorted(t)
        # return s==t




        # catch is that it will run if no need to check by each character
        # so the length should be also same in another string 

        # t_set = set(t)
        # for ch in s:
        #     if ch not in t_set: # direct find in array gonna take 0(n) TC for each element
        #                     # so converted that into set which will take only 0(1)
        #         return False
        # return True        
        