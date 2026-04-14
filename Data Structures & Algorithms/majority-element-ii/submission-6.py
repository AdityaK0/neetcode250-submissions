class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1,candidate2,count1,count2 = None,None,0,0

        # why none cause if we get array element as 0 can lead to extra counts and all

        for i in range(len(nums)):
            if nums[i] == candidate1:
                count1+=1
            elif nums[i] == candidate2:   
                count2+=1
            elif count1 == 0:
                candidate1 = nums[i]
                count1 = 1
            elif count2 == 0:
                candidate2 = nums[i]
                count2 = 1
            else:
                count1-=1
                count2-=1
        
        bound = len(nums)//3

        count1,count2 = 0,0

        for num in nums:
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+=1

        res = []

        if count1>bound:
            res.append(candidate1)
        if count2>bound:
            res.append(candidate2)

        return res                    

        # return [ candidate for candidate in [candidate1,candidate2] if nums.count(candidate)>bound]    





        # but the question it self says that cant use 0(n) Space
        # need to perform this at 0(1) space

        # hash_map = {}

        # for num in nums:
        #     hash_map[num] = hash_map.get(num,0)+1
        
        # bound = len(nums)//3

        # res = []

        # for key,val in hash_map.items():
        #     if val > bound:
        #         res.append(key)

        # return res        







        