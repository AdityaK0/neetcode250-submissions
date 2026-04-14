class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # using hashSet 

        hashSet = [0]*(len(nums)+1)
        

        for i in range(len(nums)):
            if nums[i]>len(nums) or nums[i]<0:
                continue
            hashSet[nums[i]-1] = nums[i]

        smallest_positive_number = 1
        for i in range(len(hashSet)):
            if hashSet[i]==smallest_positive_number:
                smallest_positive_number+=1

        return smallest_positive_number                





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
        