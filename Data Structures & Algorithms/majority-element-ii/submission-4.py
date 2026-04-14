class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num,0)+1
        
        bound = len(nums)//3

        res = []

        for key,val in hash_map.items():
            if val > bound:
                res.append(key)

        return res        







        