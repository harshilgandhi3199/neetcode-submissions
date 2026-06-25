import math, heapq

class Solution:
    def distFromOrigin(self, x, y):
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i, point in enumerate(points):
            distances.append((self.distFromOrigin(point[0], point[1]), i))

        heapq.heapify(distances)

        result = []
        while len(result) < k:
            # heap pop already maintains the heap property
            pair = heapq.heappop(distances)
            result.append(points[pair[1]])

        return result
        