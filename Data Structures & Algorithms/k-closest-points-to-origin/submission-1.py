import heapq

class Solution:
    # Max-Heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(maxHeap)
            result.append([x, y])

        return result