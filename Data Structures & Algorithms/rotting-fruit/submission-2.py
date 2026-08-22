class Solution:
    # Time - O(m * n)
    # Space - O(m * n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # check if input grid is non-empty
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        freshFruits = 0
        timeDuration = 0

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshFruits += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        # bfs traversal - add neighboring fresh fruits of rotten fruits to a queue
        while freshFruits > 0 and queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshFruits -= 1
                        queue.append((nr, nc))

            timeDuration += 1
        
        return timeDuration if freshFruits == 0 else -1

