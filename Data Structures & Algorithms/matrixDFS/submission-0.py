class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid,r,c , visit):
            Rows = len(grid)
            Cols = len(grid[0])
            if min(r,c) <0  or r==Rows or c==Cols or grid[r][c] ==1 or (r,c) in visit:
                return 0
            if r == Rows-1 and c == Cols -1:
                return 1
            
            visit.add((r,c))

            count =0
            count += dfs(grid , r+1,c ,visit)
            count += dfs(grid , r-1 , c ,visit)
            count += dfs(grid , r , c+1 ,visit)
            count += dfs(grid , r , c-1 , visit)

            visit.remove((r,c))
            return count
        
        return dfs(grid,0,0,set())

        