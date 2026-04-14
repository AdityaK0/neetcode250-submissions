class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0 
        # right = len(s)-1

        # while left<=right:
        #     s[left],s[right] = s[right],s[left]
        #     left+=1
        #     right-=1
        
        # using stack
        stack = []
        for ch in s:
            stack.append(ch)
        

        i = 0 
        while stack:
            s[i] = stack.pop()
            i+=1

        