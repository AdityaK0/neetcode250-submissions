class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        smallest_positive_number = 1

        i = 0
        
        while i<len(nums):
            if sorted_nums[i] == smallest_positive_number:
                # this means we already have the smallest positive number 
                # need to find the next smallest_positive_number
                smallest_positive_number+=1
            i+=1


        return smallest_positive_number         
        