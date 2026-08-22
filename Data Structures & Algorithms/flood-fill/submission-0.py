class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        rows = len(image)
        cols = len(image[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        startingPixel = image[sr][sc]
        
        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            image[r][c] = color
            visited.add((r, c))
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == startingPixel:
                    dfs(nr, nc, visited)

        dfs(sr, sc, visited)
        return image