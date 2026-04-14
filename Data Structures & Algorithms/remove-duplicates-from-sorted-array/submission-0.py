class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lastOccuredElement = nums[0]
        i = 1
        k = 1
        n = len(nums)

        while i<n:
            if nums[i] == lastOccuredElement:
                nums[i] = -1000
                i+=1
            else:
                lastOccuredElement = nums[i]
                i+=1
                k+=1


        while n>-1:
            if nums[n-1] ==  -1000:
                nums.pop(n-1)
            n-=1

        return k    








        