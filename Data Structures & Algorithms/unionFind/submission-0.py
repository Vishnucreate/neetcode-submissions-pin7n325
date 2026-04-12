class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.num_components = n 
        

    def find(self, x: int) -> int:
        
        if x !=self.parent[x]:


            self.parent[x] = self.parent[self.parent[x]]
        return self.parent[x]
        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.rank[root_x] += self.rank[root_y]
                self.parent[root_y] = root_x 
            else:
                
                self.rank[root_y] += self.rank[root_x]
                self.parent[root_x] = root_y
            self.num_components -= 1
            return True
        return False
    
        
        

    def getNumComponents(self) -> int:
        return self.num_components

