class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1l = len(word1)
        w2l = len(word2)

        i = 0
        ans = ""
        while i<w1l and i<w2l:
            ans+=word1[i]
            ans+=word2[i]

            i+=1

        if w2l>w1l:
            ans+=word2[i:]   
        elif w1l>w2l:
            ans+=word1[i:]     

        return ans    