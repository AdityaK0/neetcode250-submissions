class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #way3
        # hash_map of both string and check the value of the key
        s_map = {}
        t_map = {}

        for ch in s:
            s_map[ch] = s_map.get(ch,0)+1

        for ch in t:
            t_map[ch] = t_map.get(ch,0)+1
        large_hash_map = t_map if len(t)>len(s) else s_map 
        for key in large_hash_map:
            if key in s_map and key in t_map:
                if s_map[key]!=t_map[key]:
                    return False
            else:
                return False
        return True                       

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
        