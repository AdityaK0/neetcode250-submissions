class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1 

        # using set

        nums_set = set(nums) 
        max_length = 0
        for num in nums:
            sub_length = 0
            if num-1 not in nums_set:

                while num+sub_length in nums_set:
                    sub_length+=1
            max_length = max(max_length,sub_length)        

        return max_length


        # sorted_nums = sorted(nums)
    
        # max_consicutive = 0
        # sub_max = 1
        # for i in range(1,len(sorted_nums)):
        #     if sorted_nums[i] - sorted_nums[i-1] == 1:
        #         sub_max+=1
        #     elif sorted_nums[i] - sorted_nums[i-1] == 0:
        #         pass
        #     else:
        #         max_consicutive = max(sub_max,max_consicutive)
        #         sub_max = 1
        
        # return max(max_consicutive,sub_max)    
        
        