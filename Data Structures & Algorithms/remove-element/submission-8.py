class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        if not nums:
            return i

        while i<len(nums) and  nums[i]!=val:
            i+=1

        if i>=len(nums)-1:
            return i # number of elements which are not equals to the val

        if i<len(nums)-1:
            j=i+1

        while j<len(nums):
            if nums[j]!=val:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
                j+=1
            else:    
                j+=1

        return i                    


        # using normal loop but in this it does not shit val on the last side 
        # k = 0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[k] = nums[i]
        #         k+=1
        # return k        



        i = 0
        j = 0
        if not nums:
            return i    


        while i<len(nums) and nums[i]!=val:
            i+=1

        if not i<len(nums) or i == len(nums)-1:
            return i

        if i<len(nums)-1:
            j=i+1

        while j<len(nums):
            if nums[j]!=val:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            else:
                j+=1

        return i                 





        
        
            
        
        