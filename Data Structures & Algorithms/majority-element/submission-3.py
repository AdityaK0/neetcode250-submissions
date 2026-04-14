class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore reset the value when it comes to ZERO

        element = nums[0]
        count  = 1

        for i in range(1,len(nums)):
            if nums[i] == element:
                count+=1
            elif count == 0 :
                element = nums[i]
                count=1
            else:
                count-=1

        return element




        # nums = sorted(nums) 
        # return nums[len(nums)//2]

        # count = {}
        # res = nums[0]
        # maxCount = 0

        # for num in nums:
        #     count[num] = count.get(num,0)+1
        #     if count[num]>maxCount:
        #         res = num
        #     maxCount = max(count[num],maxCount)

        # return res    


        