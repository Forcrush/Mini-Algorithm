'''
Author: Puffrora
Date: 2020-10-25 14:58:19
LastModifiedBy: Puffrora
LastEditTime: 2020-10-25 15:12:18
'''


# . 贪心算法
# 时间复杂度 O(T+N)，其中 T 是区间的长度，N 是子区间的数量
# 空间复杂度 O(T)
class Solution:
    def videoStitching(self, clips, T):
        from collections import defaultdict

        # 记录每个起始点的最大结束点
        max_end = defaultdict(int)
        for start, end in clips:
            max_end[start] = max(max_end[start], end)
        
        last, pre, res = 0, 0, 0
        for t in range(T):
            last = max(last, max_end[t])
            if last >= T: return res + 1
            if last == t: return -1
            if t == pre:
                res += 1
                pre = last

        return res
