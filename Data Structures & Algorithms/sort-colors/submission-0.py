class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums


        # i cant return another array need to do with in the same array
        # so combine and put the data into nums
        red = []
        white = []
        blue = []

        for num in nums:
            if num==0:
                red.append(num)
            elif num==1:
                white.append(num)
            else:
                blue.append(num)
       
        combo = red+white+blue
        for i in range(len(combo)):
            nums[i] = combo[i]        
        
        return nums
        # return red+white+blue                

        