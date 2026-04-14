class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # using bucket sort 
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1

        buckets = [ [] for i in range(len(nums)+1) ] 

        # added +1 in the length cause what if array contains all same element 
        # then frequency will be equals to len(arr) but here if you dont add +1
        # then it can lead to out of bound index error cause 
        # we are trying to append values in buckets[len(nums)] = value so +1 is required

        for key,val in freq_map.items():
            buckets[val].append(key)

        res = []

        for i in range(len(buckets)-1,-1,-1):
            for key in buckets[i]:
                res.append(key)    

                if len(res)==k:
                    return res




        return [num for num,count in hash_map[:k]] 

        import heapq

        heap = []

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1
        
        res = []
        for key in freq_map:
            heapq.heappush(heap,(freq_map[key],key))

            if len(heap)>k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]

       


        