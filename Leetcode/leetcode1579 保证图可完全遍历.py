'''
Author: Puffrora
Date: 2021-03-14 08:53:31
LastModifiedBy: Puffrora
LastEditTime: 2021-03-14 09:14:59
'''


from typing import List

# Disjoint Set Union
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.n = n
        # 当前连通分量数
        self.connected_component = n
    
    def find(self, x: int) -> int:
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)
        if x_par == y_par:
            return False
        if self.rank[x_par] < self.rank[y_par]:
            x_par, y_par = y_par, x_par
        self.parent[y_par] = x_par
        self.rank[x_par] += self.rank[y_par]
        self.connected_component -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        dsu_alice, dsu_bob = DSU(n), DSU(n)
        delete = 0

        # 节点编号改为从零开始
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1
        
        # 公共边
        for t, u, v in edges:
            if t == 3:
                if not dsu_alice.union(u, v):
                    delete += 1
                else:
                    dsu_bob.union(u, v)

        # 独占边
        for t, u, v in edges:
            if t == 1:
                if not dsu_alice.union(u, v):
                    delete += 1
            if t == 2:
                if not dsu_bob.union(u, v):
                    delete += 1

        if dsu_alice.connected_component != 1 or dsu_bob.connected_component != 1:
            return -1
            
        return delete