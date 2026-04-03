class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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

       


        