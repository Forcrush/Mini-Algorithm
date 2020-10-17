'''
Author: Puffrora
Date: 2020-10-14 22:13:36
LastModifiedBy: Puffrora
LastEditTime: 2020-10-14 22:30:49
'''


"""
Hierholzer 算法可以在一个欧拉图中找出欧拉回路

我们从节点 u 开始，任意地经过还未经过的边，直到我们「无路可走」。此时我们一定回到了节点 u，这是因为所有节点的入度和出度都相等
回到节点 u 之后，我们得到了一条从 u 开始到 u 结束的回路，这条回路上仍然有些节点有未经过的出边
我们再从某个这样的节点 v 开始，继续得到一条从 v 开始到 v 结束的回路，再嵌入之前的回路中，即
u→⋯→v→⋯→u
变为
u→⋯→v→⋯→v→⋯→u
以此类推，直到没有节点有未经过的出边，此时我们就找到了一条欧拉回路
"""
class Solution:
    def crackSafe(self, n, k):
        seen = set()
        res = []
        threshold = 10 ** (n - 1)

        # node 都应该为 (n-1)位数 假设对于 n=3 k=5 某个node为 24
        def dfs(node):
            for x in range(k):
                # 若 x=3 下一个 node 为 243
                next_node = 10 * node + x
                if next_node not in seen:
                    seen.add(next_node)
                    # 取余得 43 则以 43 为节点继续搜索
                    dfs(next_node % threshold)
                    res.append(str(x))

        dfs(0)
        
        # 回到起点 起点为 0 因此要加上 "0" * (n - 1)
        return "".join(res) + "0" * (n - 1)

