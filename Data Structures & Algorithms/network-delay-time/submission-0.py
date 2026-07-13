import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a graph
        graph = defaultdict(list)
        for u, v, t in times:
            if u not in graph:
                graph[u] = [(v, t)]
            else:
                graph[u].append((v, t))
         
        distances = {k: 0}
        heap = [(0, k)]

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distances.get(node, float('inf')):
                continue
            
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        if len(distances) != n:
            return -1

        minTime = 0
        for value in distances.values():
            minTime = max(minTime, value)

        return minTime