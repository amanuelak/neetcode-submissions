class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = defaultdict(int)

        for num in nums: #O(n)
            freq_map[num] +=1

        heap = []

        for num, freq in freq_map.items(): #O(m), worst case: m = n
            heapq.heappush(heap, (freq, num)) #O(log m)

            if len(heap) > k: #O(log m - k)
                heapq.heappop(heap)
            
        
        return [num for freq, num in heap] # O(m)



        # O(n + m log m + m)
        #O(nlogn)