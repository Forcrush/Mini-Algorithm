'''
Author: Puffrora
Date: 2020-10-17 11:00:56
LastModifiedBy: Puffrora
LastEditTime: 2020-10-17 18:57:54
'''


"""
我们对字符串 A 和 B 构造一个包含 6 个节点 a, b, c, d, e, f 的基础图。
对于字符串中的第 i 位 A[i] 和 B[i]，我们在基础图中连一条 A[i] -> B[i] 
的有向边，允许重边和自环。如果字符串 A 和 B 相等，那么基础图中就只有自环。

我们来考虑交换 A[i] 和 A[j] 会导致图如何变化。例如当 A 为 'ca'...'，
B 为 'ab' 时，基础图中有边 c -> a 和 a -> b。如果我们交换 A[0] 和 A[1]，
那么图中会剩下边 c -> b 和 a 的自环。我们把这种“把两条首尾相连的边变成一条
新边和一个自环”的操作称为“截断”。可以证明，最优的操作中，所有的操作都是截断
操作（证明的方法大致为：首先在任意时刻，图中必须有两条首尾相连的边存在；
其次我们的目标是把所有的边变成自环，那么除了 a -> b 和 b -> a 这种情况之外，
其它所有的一次操作最多只能使得图中多出一个自环，因此截断操作是最优的）。

最后我们考虑将基础图拆分为若干个环，拆分的方法并不是唯一的。对于一个长度为 k 的环，
我们可以用 k - 1 次截断操作，把环上所有的边变为自环。因此，如果基础图被拆分为长度为 
C1, C2, ... Ck 的 k 个环，需要的截断操作次数为 ∑(Ck-1), 这个求和也等于基础图中非
自环的边数 n0 减去环的个数 k。因此，我们的目标对基础图进行一个环数最多的拆分。

当我们把基础图 G 拆分为环并进行截断操作时，我们可以每次截断从左到右第一个 A[i] != B[i] 
对应的那条边。即在字符串 A 和 B 中，我们每次找到最左侧满足 A[i] != B[i] 的 i，
并搜索满足 j > i 且 A[j] == B[i] 的 j，然后交换 A[i] 和 A[j] 得到优化后的下一个状态
通过这种做法，我们可以使用广度优先搜索遍历所有的状态

方法二 https://leetcode-cn.com/problems/k-similar-strings/solution/xiang-si-du-wei-k-de-zi-fu-chuan-by-leetcode/

"""
class Solution:
    def kSimilarity(self, A, B):
        from collections import deque

        def neighbor(S):
            for i, v in enumerate(S):
                if v != B[i]:
                    break
            
            T = list(S)
            for j in range(i+1, len(S)):
                if S[j] == B[i]:
                    T[i], T[j] = T[j], T[i]
                    yield "".join(T)
                    T[i], T[j] = T[j], T[i]

        queue = deque([A])
        seen = {A: 0}
        while queue:
            S = queue.popleft()
            if S == B: return seen[S]
            for T in neighbor(S):
                if T not in seen:
                    seen[T] = seen[S] + 1
                    queue.append(T)



