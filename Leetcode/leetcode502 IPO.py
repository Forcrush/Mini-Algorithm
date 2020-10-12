'''
Author: Puffrora
Date: 2020-10-11 16:47:16
LastModifiedBy: Puffrora
LastEditTime: 2020-10-11 17:00:49
'''


# 时间复杂度 O(klogN)
# 空间复杂度 O(N)
class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        import heapq

        if not Profits: return W

        pro_heap = []
        cur = W
        for i in range(len(Profits)):
            heapq.heappush(pro_heap, (-Profits[i], Capital[i]))
        
        for _ in range(k):

            tmp = []
            while pro_heap and pro_heap[0][1] > cur:
                tmp.append(heapq.heappop(pro_heap))

            if not pro_heap: return cur

            item = heapq.heappop(pro_heap)
            cur += abs(item[0])

            for t in tmp:
                heapq.heappush(pro_heap, t)
        
        return cur

