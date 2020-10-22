'''
Author: Puffrora
Date: 2020-10-22 19:41:39
LastModifiedBy: Puffrora
LastEditTime: 2020-10-22 19:57:17
'''


"""
贪心策略
先将所有区间按照起点降序，终点升序排列，这样排序的好处是在遍历的过程中只需要关注集合中最小的两个数字

遍历时根据当前区间[start, end]和交集中两个最小数字min1, min2的关系，分情况讨论：

1)、min1、min2都不在区间内，
集合中应该加入start和start+1两个数字，同时更新min1、min2为这两个数字

2)、min1、min2都在区间内，不需更新

3)、只有min1在区间内，
如果min1==start, 集合加入start+1，同时min2更新为start+1
否则min2更新为min1， min1更新为start， 集合加入start

4)、只有min2在区间内，
如果min2==start, 集合加入start+1，同时min1更新为start，min2更新为start+1
否则min1更新为start， 集合加入start

时间复杂度O(n*logn + n) = O(nlgn), 主要为排序的复杂度，排序后只是一次遍历
空间复杂度为set集合的复杂度，set元素不会超过 2*n， 所以空间复杂度为O(n)

"""
class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (-x[0], x[1]))
        res, min1, min2 = 0, float('inf'), float('inf')

        for a, b in intervals:
            # 都在
            if a <= min1 <= b and a <= min2 <= b:
                continue
            
            # 较小的 min1 在
            elif a <= min1 <= b:
                res += 1
                if min1 == a:
                    min2 = a + 1
                else:
                    min1, min2 = a, min1

            # 较大的 min2 在
            elif a <= min2 <= b:
                res += 1
                if min2 == a:
                    min1, min2 = min2, a + 1
                else:
                    min1 = a

            # 都不在
            else:
                res += 2
                min1, min2 = a, a + 1
        
        return res