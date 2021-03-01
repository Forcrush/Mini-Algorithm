'''
Author: Puffrora
Date: 2021-03-01 20:43:32
LastModifiedBy: Puffrora
LastEditTime: 2021-03-01 20:54:52
'''


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        from collections import defaultdict, deque

        node = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    node[i].append(j)
                    node[j].append(i)
        
        have = set([i for i in range(n)])
        province = 0
        while have:
            province += 1

            # BFS and elimination
            queue = deque([have.pop()])
            while queue:
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    for n in node[cur]:
                        if n in have:
                            have.discard(n)
                            queue.append(n)
        
        return province

