class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixMap = {}
        prefixMap[0] = 1

        curr_sum = 0
        subArrayPossibilityCount = 0

        for i in range(len(nums)):
            curr_sum+=nums[i]

            if curr_sum-k in prefixMap:
                subArrayPossibilityCount+=prefixMap[curr_sum-k]

            prefixMap[curr_sum] = prefixMap.get(curr_sum,0)+1

        return subArrayPossibilityCount        

        