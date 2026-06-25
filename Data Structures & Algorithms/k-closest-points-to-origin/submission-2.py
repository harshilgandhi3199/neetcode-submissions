import heapq

class Solution:
    # Time - O(n log k + k log k) | Space - O(k)
    # Max-Heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(maxHeap, (-dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # no need to do heap pop here. 
        # heap already contains k closest points
        # result = []
        # for _ in range(k):
        #     _, x, y = heapq.heappop(maxHeap)
        #     result.append([x, y])

        return [[x, y] for _, x, y in maxHeap]