class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # ideal way for interview 

        prefix = strs[0]

        for i in range(1,len(strs)):

            j = 0

            while j<len(prefix) and j<len(strs[i]) and prefix[j] == strs[i][j]:
                j+=1

            prefix = prefix[:j]
            if not prefix:
                return ""

        return prefix             


        # i performed on leet

        first = strs[0]

        for i in range(1,len(strs)):
            ans = ""
            for j in range(min(len(first),len(strs[i]))):
                if first[j] == strs[i][j]:
                    ans+=strs[i][j]
                else:
                    break
            first = ans

        return first            





         
        #own way 

        # fstr = strs[0]
        # mini = float("inf")

        # for i in range(len(strs)):
        #     cstr = strs[i]

        #     k = 0
        #     ctn = 0

        #     while k<len(cstr) and k<len(fstr):
        #         if cstr[k] == fstr[k]:
        #             ctn+=1
        #         else:
        #             mini = min(mini,k)if mini != float("inf") else k
        #             break
        #         k+=1

        #     mini = min(mini,ctn)

        # return fstr[0:mini]              

        
        