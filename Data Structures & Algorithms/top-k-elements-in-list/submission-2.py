import heapq

class Solution:
    # Time - O(n log k) | Space - O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a freq map
        # create min-heap
        # for each num in freq map:
            #push (freq, num) into heap
            #if heap size > k, pop once to remove the smalled freq
        # after all nums are processed, heap contains k pairs
        # pop all pairs from heap and collect in output list
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result