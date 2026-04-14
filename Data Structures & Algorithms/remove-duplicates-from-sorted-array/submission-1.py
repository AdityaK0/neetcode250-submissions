class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        ele = nums[0]
        pos = 1
        for i in range(1,len(nums)):
            if nums[i]!=ele:
                nums[pos] = nums[i]
                ele = nums[i]
                pos+=1

        return pos        




        # lastOccuredElement = nums[0]
        # i = 1
        # k = 1
        # n = len(nums)

        # while i<n:
        #     if nums[i] == lastOccuredElement:
        #         nums[i] = -1000
        #         i+=1
        #     else:
        #         lastOccuredElement = nums[i]
        #         i+=1
        #         k+=1


        # while n>-1:
        #     if nums[n-1] ==  -1000:
        #         nums.pop(n-1)
        #     n-=1

        # return k    








        