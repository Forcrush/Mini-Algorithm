'''
Author: Puffrora
Date: 2020-10-12 20:18:12
LastModifiedBy: Puffrora
LastEditTime: 2020-10-12 21:36:44
'''

'''
输入数据 graph = [(n1, n2, w), (n2, n3, w), ...]
每个元素代表一条有向边
数据存储用双重字典 graph = {sn1: {en1: w1, en2: w2, ...}, sn2: {en1: w1, en2: w2, ...}, ...}

========================================================================
对比图
            Dijisktra       Floyd       Bellman-Ford        SPFA
时间复杂度  O((M+N)logN)    O(N**3)         O(NM)           最坏O(NM)
空间复杂度      O(M)        O(N**2)         O(M)              O(M)
负权边处理      ×              √             √                 √
判定负环        ×              ×             √                 √
适用情况        S1             S1            S2                S2

* S1: 稠密图 和顶点关系密切
* S2: 稀疏图 和边关系密切

Reference Link: https://www.cnblogs.com/thousfeet/p/9229395.html
========================================================================
'''
from collections import defaultdict


def initialization(graph):
    final_graph = defaultdict(dict)
    for sn, en, w in graph:
        final_graph[sn][en] = w
        # 保证所有点都能作为键值 这样字典键值数等于节点数
        final_graph[sn][sn] = 0
        final_graph[en][en] = 0
    
    return final_graph


def Dijkstra(graph, a, b):

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
        
        # 存在未遍历节点中离起点最近的点
        if min_node != None:
            visited[min_node] = True

            # 对 min_node 所有出边进行松弛
            for k,v in graph[min_node].items():
                if dist[min_node] + v < dist[k]:
                    dist[k] = dist[min_node] + v

    # print(dist)

    return dist[b]


def Floyd(graph, a, b):
    dist = [[float('inf') for _ in range(len(graph))] for _ in range(len(graph))]
    # 根据原始图初始化点间距离
    for sn, en in graph.items():
        dist[sn][sn] = 0
        for e, w in en.items():
            dist[sn][e] = w
    
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # print(dist)

    return dist[a][b]


def Bellman_Ford(graph, a, b):
    dist = [float('inf')] * len(graph)
    dist[a] = 0

    # 因为两点间的最短路最多包含 n-1 条边因此进行 n-1 轮松弛
    for _ in range(len(graph)-1):
        no_relaxation = True
        # 遍历每一条边
        for sn, en in graph.items():
            for e, w in en.items():
                if dist[sn] + w < dist[e]:
                    dist[e] = dist[sn] + w
                    no_relaxation = False
        
        # 如果某一轮松弛操作中没有边进行松弛 说明路径已更新完 可以提前终止
        if no_relaxation:
            break
    
    # 可以额外进行 1 轮松弛来判断是否存在负环
    for _ in range(1):
        for sn, en in graph.items():
            for e, w in en.items():
                if dist[sn] + w < dist[e]:
                    print("Negative Loop Exists !")
                    return
    # print(dist)

    return dist[b]


# 可看作优化的 Bellman-Ford 算法
# 每一遍松弛中不是考虑所有边 而只是考虑前一遍松弛中改变了最短路估计值的结点 因为只有他们才可能引起其邻接点最短路估计值发生改变
def SPFA(graph, a, b):
    dist = [float('inf')] * len(graph)
    dist[a] = 0

    queue = [a]
    # 记录节点入队次数
    in_queue_time = defaultdict(int)
    in_queue_time[a] += 1

    while queue:
        cur = queue.pop(0)
        for e, w in graph[cur].items():
            # 如果 cur 的某条出边能够松弛
            if dist[cur] + w < dist[e]:
                dist[e] = dist[cur] + w
                # 如果这条边终点不在队列中则入队
                if e not in queue:
                    queue.append(e)
                    in_queue_time[e] += 1
                    # 如果某个点入队次数大于 n 则说明存在负环
                    if in_queue_time[e] > len(graph):
                        print("Negative Loop Exists !")
                        return

    # print(dist)

    return dist[b]


# @ testing
test = [(0, 1, 4), (1, 2, 9), (2, 3, 7), (0, 2, 1), (3, 0, 2)]
g = initialization(test)

print(Dijkstra(g, 0, 3))
print(Floyd(g, 0, 3))
print(Bellman_Ford(g, 0, 3))
print(SPFA(g, 0, 3))
