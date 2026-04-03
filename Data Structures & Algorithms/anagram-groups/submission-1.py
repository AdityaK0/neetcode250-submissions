from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [ [strs[0]] ]
        

        hash_map = defaultdict(list)
        result = []     

        for i in range(len(strs)):
            if not hash_map[str(sorted(strs[i]))]:
                hash_map[str(sorted(strs[i]))] = [i]
            else:
                hash_map[str(sorted(strs[i]))].append(i)

        for key in hash_map:
            anagram_group = []
            for index in hash_map[key]:
                anagram_group.append(strs[index])
            result.append(anagram_group)

        return result        





        # result = []    
        # already_grouped=set()

        # for i in range(len(strs)):
        #     if str(sorted(strs[i])) not in already_grouped:
        #         anagram_group = [strs[i]]
        #         for j in range(i+1,len(strs)):
        #             if sorted(strs[i]) == sorted(strs[j]):
        #                 anagram_group.append(strs[j])
        #                 already_grouped.add(str(sorted(strs[j])))
        #         result.append(anagram_group) 


        # return result            


        