class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        if not nums or len(nums)==1:
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





        
        
            
        
        