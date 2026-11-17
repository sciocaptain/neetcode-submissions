class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def valid(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                grid[r][c] == '0' or
                (r, c) in visited
            ):
                return False
            return True

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (not valid(nr, nc)):
                        continue
                    q.append((nr, nc))
                    visited.add((nr,nc))
            return

            

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands
                