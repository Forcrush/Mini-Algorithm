'''
Author: Puffrora
Date: 2021-03-09 13:27:26
LastModifiedBy: Puffrora
LastEditTime: 2021-03-09 13:37:07
'''


from typing import List


# 注意题目输入必定是一个完美的山脉数组（有且只有一个峰顶 无平原） 才能用此简单的二分法
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        start, end = 0, len(A)-1

        while start < end:
            mid = (start + end) // 2
            if A[mid] < A[mid+1]:
                start = mid + 1
            else:
                end = mid
        
        return start
