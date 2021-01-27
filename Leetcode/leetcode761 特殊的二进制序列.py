'''
Author: Puffrora
Date: 2021-01-27 18:40:53
LastModifiedBy: Puffrora
LastEditTime: 2021-01-27 19:30:18
'''


class Solution:
    def makeLargestSpecial(self, S):

        import heapq as hq
        
        S = list(S)
        pairs = [0] * len(S)
        stack = []
        for i, c in enumerate(S):
            if c == '1':
                stack.append(i)
            elif c == '0':
                pairs[stack.pop()] = i
        
        def arrange(s, l, r):
            if l > r: return

            heap = []
            i = l
            while i < r:
                arrange(s, i+1, pairs[i]-1)

                # 当前 [i, pairs[i]] 区间已是排好序的特殊二进制串
                hq.heappush(heap, s[i:pairs[i]+1])

                # 移动到下一个子串开头
                i = pairs[i] + 1
            
            # 因为 heap 是根据字典序从小到大弹出子串 而我们需要从大到小排列子串
            p = r
            while heap:
                head = hq.heappop(heap)
                for c in range(len(head)-1, -1, -1):
                    s[p] = head[c]
                    p -= 1

        arrange(S, 0, len(S)-1)

        return ''.join(S)


