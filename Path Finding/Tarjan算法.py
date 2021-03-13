'''
Author: Puffrora
Date: 2021-03-13 09:38:09
LastModifiedBy: Puffrora
LastEditTime: 2021-03-13 15:34:51
'''
# @ leetcode 1568 Tarjan寻找图中割点
# @ 下列代码作用: 在图中查找强连通分量


from collections import defaultdict


"""
0 -----> 1 -----> 4 ----->  5
| |\     |                  |
|    \   |                  |
v      \ v                  v
2 -----> 3                  6
"""
edges = [(0, 1), (0, 2), (2, 3), (1, 3), (3, 0), (1, 4), (4, 5), (5, 6)]


def initialization(edge):
    node = defaultdict(list)
    for s, e in edge:
        node[s].append(e)
        # 使字典键数等于节点数
        node[e].extend([])
    
    return node


G  = initialization(edges)

# 搜索节点计数
global count
count = 0
# 节点数
N = len(G)
# 记录回溯值 即能到此点的最小序号点
low = [0] * N
# 记录 dfs 中的时间戳
dfn = [0] * N
# 记录搜索过程压入栈的元素
stack = []
# 记录是否在栈中
in_stack = [0] * N
# 记录找到的强连通分量
res = []


def tarjan(i):
    global count
    low[i] = count
    dfn[i] = count
    count += 1
    stack.append(i)
    in_stack[i] = 1

    for j in G[i]:
        # j 没有被访问过
        if not dfn[j]:
            tarjan(j)
            # 更新能找的到祖先
            if low[j] < low[i]:
                low[i] = low[j]
        else:
            # in_stack[j] 这个判断条件很重要 这样可以避免已经确定在其他联通图的 j 因为 i 到 j 的单向边而影响到 low[i]
            if dfn[j] < low[i] and in_stack[j]:
                low[i] = dfn[j]

    #  往后回溯的时候如果发现 dfn 和 low 相同的节点 就可以把这个节点之后的节点全部弹栈构成连通图
    if dfn[i] == low[i]:
        tmp = set()
        while True:
            cur = stack.pop()
            tmp.add(cur)
            in_stack[cur] = 0

            if cur == i:
                break
        res.append(tmp)


if __name__ == '__main__':
    for i in range(N):
        if not dfn[i]:
            tarjan(i)

    print("强连通分量:")
    for i in res:
        print(i)
