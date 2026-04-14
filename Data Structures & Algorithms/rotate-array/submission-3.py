class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # without 0(n) space

        n = len(nums)
        k = k%n
        def reverse(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)     


        # temp = []
        # n = len(nums)

        # k = k%n

        # for i in range(n-k,n,1):
        #     temp.append(nums[i])

        # for i in range(n-k):
        #     temp.append(nums[i])

        # for i in range(len(nums)):
        #     nums[i] = temp[i]    


