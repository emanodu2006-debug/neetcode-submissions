class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq

        heap = []
        count = Counter(nums)

        for key, freq in count.items():
            heapq.heappush(heap, (freq, key))

            if len(heap) > k:
                heapq.heappop(heap)

            
        return[num for key, num in heap]
