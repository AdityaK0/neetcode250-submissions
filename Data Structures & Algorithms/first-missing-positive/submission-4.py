class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # using index marking with o(1) space

    
       # step 1 : replace non-eligible smallest positive integer
        isOneContains = False
        for i in range(len(nums)):
            if nums[i] == 1:
                isOneContains = True
            elif nums[i]<1 or nums[i]>len(nums):
                nums[i] = 1

        if not isOneContains:
            return 1        
        
        # step 2 : implement negation on each element

        for i in range(len(nums)):
            num = abs(nums[i]) # to find the index we obviously need positive num
            index = num-1
            
            if not nums[index]<0:
               nums[index] = nums[index]*-1

        # ste3 : find if element is greator then 0 which means it is the smallest
        # positive number

        for i in range(len(nums)):
            if nums[i]>0:
                return i+1

        return len(nums)+1 # what if the smallest positive number is not in the array
                          # it means if not in the array then the answer is len(nums)+1               




        # using hashSet 

        # hashSet = [0]*(len(nums)+1)
        

        # for i in range(len(nums)):
        #     if nums[i]>len(nums) or nums[i]<0:
        #         continue
        #     hashSet[nums[i]-1] = nums[i]

        # smallest_positive_number = 1
        # for i in range(len(hashSet)):
        #     if hashSet[i]==smallest_positive_number:
        #         smallest_positive_number+=1

        # return smallest_positive_number                





        # sorted_nums = sorted(nums)
        # smallest_positive_number = 1

        # i = 0
        
        # while i<len(nums):
        #     if sorted_nums[i] == smallest_positive_number:
        #         # this means we already have the smallest positive number 
        #         # need to find the next smallest_positive_number
        #         smallest_positive_number+=1
        #     i+=1


        # return smallest_positive_number         
        