class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets solve it using one array with 0(n) space

        prefix = [0]*len(nums)
        prefix[0] = 1

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        right = 1

        for i in range(len(nums)-1,-1,-1):
            prefix[i] = prefix[i]*right
            right*=nums[i]

        return prefix        

        # still array we afre creating 3 array here
        # prefix = [0]*len(nums)
        # prefix[0] = 1
        
        # for i in range(1,len(nums)):
        #     prefix[i] = prefix[i-1]*nums[i-1]
        
        # suffix = [0]*len(nums)
        # suffix[-1] = 1
        
        # for i in range(len(nums)-2,-1,-1):
        #     suffix[i] = suffix[i+1]*nums[i+1]
        
        # res = [] 
        
        # for i in range(len(nums)):
        #     res.append(prefix[i]*suffix[i])
        
        # return res 


        # curr_index = 0
        # res = []
        # while curr_index<len(nums):

        #     curr_index_after = curr_index+1
            
        #     curr_index_product = 1

        #     while curr_index_after<len(nums):
        #         curr_index_product*=nums[curr_index_after]
        #         curr_index_after+=1

        #     curr_index_previous = curr_index-1

        #     while curr_index_previous>-1:
        #         curr_index_product*=nums[curr_index_previous]
        #         curr_index_previous-=1
            
        #     res.append(curr_index_product)
        #     curr_index+=1

        # return res



