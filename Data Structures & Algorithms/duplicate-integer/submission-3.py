class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}
    
        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1
            if hash_map[num]>1:
                return True
        return False        
        
        # currently no need for this cause if u see above 
        # after assigning the count we check at same time too
        # for val in hash_map.values():
        #     if val > 1: 
        #         return True
        
        
        # return False

        #brute 
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False            



        # for sorted array not for this one
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True

        # return False        
