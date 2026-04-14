class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_index = 0
        res = []
        while curr_index<len(nums):

            curr_index_after = curr_index+1
            
            curr_index_product = 1

            while curr_index_after<len(nums):
                curr_index_product*=nums[curr_index_after]
                curr_index_after+=1

            curr_index_previous = curr_index-1

            while curr_index_previous>-1:
                curr_index_product*=nums[curr_index_previous]
                curr_index_previous-=1
            
            res.append(curr_index_product)
            curr_index+=1

        return res



