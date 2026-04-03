class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        fstr = strs[0]
        mini = float("inf")

        for i in range(len(strs)):
            cstr = strs[i]

            k = 0
            ctn = 0

            while k<len(cstr) and k<len(fstr):
                if cstr[k] == fstr[k]:
                    ctn+=1
                else:
                    mini = min(mini,k)if mini != float("inf") else k
                    break
                k+=1

            mini = min(mini,ctn)

        return fstr[0:mini]              

        
        