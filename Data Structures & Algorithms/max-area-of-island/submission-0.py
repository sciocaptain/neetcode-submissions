class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        max_area = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        def dfs(r,c):
            if (
                r < 0 or r >= len(grid) or
                c < 0 or c >= len(grid[0]) or
                grid[r][c] == 0 or
                (r,c) in visited 
            ):
                return 0
            
            visited.add((r, c))
            area = 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == 1 and (r,c) not in visited):
                    result = dfs(r,c)
                    print("RESULT: ", result)
                    max_area = max(result, max_area)
        return max_area