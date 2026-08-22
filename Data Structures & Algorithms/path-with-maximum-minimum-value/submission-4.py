class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # here the goal is to maximize the cost of path from src to dst
        # For this, we can tweak the standard dijkstra's algorithm to always
        # visit the most expensive unvisited node
        # instead of min heap, we use a max heap which will always point us to the 
        # most expensive neighbor
        # we keep track of min value in the path
        # when we first come across the dst node, we return min value as the score
        # of the path
        #This greedy approach ensures that when you first reach the destination, you've found the path that maintains the highest possible minimum value.
        # state: (value, i, j)
        # update cond: new_value = value
        # if new_value > grid[i][j]: update
        # if value < grid[i][j]: continue
        score = float('inf')
        rows, cols = len(grid), len(grid[0])
        dist = [[float('-inf')] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]

        heap = [(-grid[0][0], 0, 0)]

        while heap:
            value, r, c = heapq.heappop(heap)
            score = min(score, -value)

            if r == rows - 1 and c == cols - 1:
                return score

            if -value < dist[r][c]:
                continue
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_value = grid[nr][nc]
                    if new_value > dist[nr][nc]:
                        dist[nr][nc] = new_value
                        heapq.heappush(heap, (-new_value, nr, nc))

        return score

