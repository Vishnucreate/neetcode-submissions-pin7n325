from typing import List

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}

        for i in range(n):
            adj[i] = []

        for src, dest in edges:
            adj[src].append(dest)
        
        topSort = []
        visit = set()
        temp_mark = set()  # Used to detect cycles
        
        for i in range(n):
            if i not in visit:
                if not self.dfs(i, adj, visit, temp_mark, topSort):
                    return []  # Return an empty list if a cycle is detected
        
        topSort.reverse()
        return topSort
    
    def dfs(self, src, adj, visit, temp_mark, topSort):
        if src in temp_mark:
            return False  # Cycle detected
        if src in visit:
            return True
        
        temp_mark.add(src)
        for neighbour in adj[src]:
            if not self.dfs(neighbour, adj, visit, temp_mark, topSort):
                return False
        
        temp_mark.remove(src)
        visit.add(src)
        topSort.append(src)
        return True

# Example usage:
sol = Solution()
n = 6
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
print(sol.topologicalSort(n, edges))  # Output should be [0, 1, 2, 3, 4, 5]
