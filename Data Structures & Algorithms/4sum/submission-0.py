class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        nums = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                m = j+1
                k = n-1

                while m<k:
                    total = nums[i]+nums[j]+nums[m]+nums[k]

                    if total>target:
                        k-=1    
                    elif total < target:
                        m+=1
                    else:
                        res.append([nums[i],nums[j],nums[m],nums[k]])
                        m+=1
                        k-=1

                        while m<k and nums[m]==nums[m-1] :
                            m+=1

                        while m<k and nums[k] == nums[k+1]:
                            k-=1

        return res                     


