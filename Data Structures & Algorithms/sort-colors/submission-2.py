class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums

        # best and optimized way is Dutch national flag algorithm
        # basically push the lower value at left and higher at right


        right = len(nums)-1
        left = 0
        current_index = 0

        while current_index<=right:
            if nums[current_index] == 0:
                nums[left],nums[current_index] = nums[current_index],nums[left]
                left+=1
                current_index+=1
            elif nums[current_index] == 2:
                nums[right],nums[current_index] = nums[current_index],nums[right]
                right-=1
            else:
                current_index+=1



       

        # another way i used in leetcode was get 3 variable increase 
        #their count as the respective color found then 
        # iterate over each from red to white to blue and update the nums
        # the iteration will done using while loop with i value will
        #be used among all 3 iteration to track the current position of 
        # nums

        # i cant return another array need to do with in the same array
        # so combine and put the data into nums
        # red = []
        # white = []
        # blue = []

        # for num in nums:
        #     if num==0:
        #         red.append(num)
        #     elif num==1:
        #         white.append(num)
        #     else:
        #         blue.append(num)
       
        # combo = red+white+blue
        # for i in range(len(combo)):
        #     nums[i] = combo[i]        
        
        # return nums
        # return red+white+blue                

        