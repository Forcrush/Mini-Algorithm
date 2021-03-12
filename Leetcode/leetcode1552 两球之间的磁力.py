'''
Author: Puffrora
Date: 2021-03-12 19:04:52
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 19:20:30
'''


from typing import List


# 二分搜索 最小距离
# 时间复杂度 O(nlognS) = O(nlogn + nlogS) S为位置上限大小即 max(position), n为篮子数即 len(position)
# 空间复杂度 O(nlogn)
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        res = -1
        left, right = 1, position[-1] - position[0]

        # 检查 dis 作为最小距离时是否可以容下 m 个球
        # 若可以说明 dis 可以更大 反之更小
        def satisfy(dis):
            start = ball = 0
            for end in range(len(position)):
                if position[end] - position[start] >= dis:
                    start = end
                    ball += 1
            
            # 算上初始位置有一个球
            ball += 1

            return ball >= m


        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if satisfy(mid):
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return res


