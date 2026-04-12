class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj={}

        for i in range(n):
            adj[i] = []

        for n1,n2,weight in edges:
            adj[n2].append([n1,weight])
            adj[n1].append([n2,weight])

        minheap = [(0,0)]
        res =0
        visit =set()
        

        while minheap and len(visit) <n:
            weight , v = heapq.heappop(minheap)
            if v in visit:
                continue
            res+= weight

            visit.add(v)
            for neighbour , weight in adj[v]:
                heapq.heappush(minheap,[weight , neighbour])
        return res if len(visit) ==n else -1


        