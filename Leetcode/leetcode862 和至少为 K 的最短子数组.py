'''
Author: Puffrora
Date: 2020-12-03 15:22:34
LastModifiedBy: Puffrora
LastEditTime: 2020-12-08 08:48:54
'''

'''
如果数组中的数据均为非负数的话，那么就对应常规的子数组和问题，可以使用滑动窗口来解决。
但是添加了负数之后，窗口的滑动便丢失了单向性，因此无法使用滑动窗口解决

单调双端队列：
我们用数组 P 表示数组 A 的前缀和，即 P[i] = A[0] + A[1] + ... + A[i - 1]。
我们需要找到 x 和 y，使得 P[y] - P[x] >= K 且 y - x 最小。

我们维护一个关于前缀和数组 P 的单调队列，它是一个双端队列，其中存放了下标 x：x0, x1, ... 
满足 P[x0], P[x1], ... 单调递增。当我们遇到了一个新的下标 y 时，我们会在队尾移除若干元素，
直到 P[x0], P[x1], ..., P[y] 单调递增。同时，我们会在队首也移除若干元素，如果 P[y] >= P[x0] + K，
则将队首元素移除，直到该不等式不满足。
'''
# 时间复杂度：O(N)
# 空间复杂度：O(N)
class Solution:
    def shortestSubarray(self, A, K):
        
        from collections import deque

        monoqueue = deque()
        res = float('inf')
        prefix_sum = [0]
        for n in A:
            prefix_sum.append(prefix_sum[-1]+n)

        for y, py in enumerate(prefix_sum):
            while monoqueue and py <= prefix_sum[monoqueue[-1]]:
                monoqueue.pop()
            
            while monoqueue and py - prefix_sum[monoqueue[0]] >= K:
                res = min(res, y-monoqueue.popleft())
            
            monoqueue.append(y)
            
        return -1 if res == float('inf') else res

