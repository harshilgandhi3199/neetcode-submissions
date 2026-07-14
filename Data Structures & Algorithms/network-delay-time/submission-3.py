class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[k - 1] = 0

        for _ in range(n - 1):
            for u, v, t in times:
                if distances[u - 1] + t < distances[v - 1]:
                    distances[v - 1] = distances[u - 1] + t

        max_dist = max(distances)
        return max_dist if max_dist < float('inf') else -1