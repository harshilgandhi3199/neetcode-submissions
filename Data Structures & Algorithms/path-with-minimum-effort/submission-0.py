class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # here the goal is to minimize the max effort along a path
        # in other words, we want to minimize the single hardest step along the path
        # in std dijkstra's we minimized the sum of edge weights from src to dst
        # here, we minimize the max effort from src to dst
        # which means when we pop the node from heap, we know that the max effort of the path
        # that goes through this cell is going to >= E and no future path to that cell
        # can do better
        # update criteria: new_effort = max(effort[curr], w)
        # where w = abs difference between next and curr node
        # if new_effort < effort[next]: effort[next] = new_effort; push to the heap
        # state: (effort, row, col)
        # we stop when we first pop the dst node
        heap = [(0, 0, 0)]
        rows, cols = len(heights), len(heights[0])

        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        # Directions: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            curr_effort, row, col = heapq.heappop(heap)
            
            if row == rows - 1 and col == cols - 1:
                return curr_effort

            # skip: already found better path
            # skip an outdated entry
            if curr_effort > efforts[row][col]:
                continue

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(curr_effort, abs(heights[row][col] - heights[nr][nc]))

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))

        return efforts[rows - 1][cols - 1]