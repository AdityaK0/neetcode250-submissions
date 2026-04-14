class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        j = 0

        while i<len(nums) and nums[i]!=val:
            i+=1

        if i>=len(nums)-1:
            return i # whats the point if we are at last index val is already at last
        else:
            j = i+1

        while j<len(nums):
            if nums[j]!=val:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
            j+=1

        return i                    

