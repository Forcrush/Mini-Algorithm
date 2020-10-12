'''
Author: Puffrora
Date: 2020-10-12 21:09:33
LastModifiedBy: Puffrora
LastEditTime: 2020-10-12 21:37:00
'''


class Solution:
    def networkDelayTime(self, times, N, K):

        from collections import defaultdict
        graph = defaultdict(dict)
        # 让节点从 0 开始 因此原节点编号需要减一
        for sn, en, w in times:
            graph[sn-1][en-1] = w
        
        for i in range(N):
            graph[i][i] = 0

        def Dijkstra(graph, a):

            dist = [float('inf')] * len(graph)
            visited = [False] * len(graph)
            # 从起始点和其连接边开始
            visited[a] = True
            dist[a] = 0
            for k,v in graph[a].items():
                dist[k] = v
            
            # 除了起点还有 n-1 个未知点需要检查 最多遍历 n-1 遍
            for _ in range(len(graph)-1):
                
                min_node = None
                # 寻找未遍历节点中离起点最近的点
                min_val = float('inf')        
                for j in range(len(dist)):
                    if not visited[j] and dist[j] < min_val:
                        min_val = dist[j]
                        min_node = j
                
                if min_node != None:
                    visited[min_node] = True

                    # 对 min_node 所有出边进行松弛
                    for k,v in graph[min_node].items():
                        if dist[min_node] + v < dist[k]:
                            dist[k] = dist[min_node] + v

            return dist

        dist = Dijkstra(graph, K-1)

        max_val = max(dist)

        return max_val if max_val < float('inf') else -1


