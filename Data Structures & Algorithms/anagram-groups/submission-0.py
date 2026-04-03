class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [ [strs[0]] ]

        result = []    
        already_grouped=set()

        for i in range(len(strs)):
            if str(sorted(strs[i])) not in already_grouped:
                anagram_group = [strs[i]]
                for j in range(i+1,len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        anagram_group.append(strs[j])
                        already_grouped.add(str(sorted(strs[j])))
                result.append(anagram_group) 


        return result            


        