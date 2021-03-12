'''
Author: Puffrora
Date: 2021-03-12 13:22:04
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 14:59:14
'''


from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        intersection = []
        p1 = p2 = 0
        l1, l2 = len(nums1), len(nums2)
        while p1 < l1 and p2 < l2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                intersection.append(nums1[p1])
                p1 += 1
                p2 += 1
        
        if not intersection: return max(sum(nums1), sum(nums2))
        p1 = p2 = cur = 0
        sum1 = sum2 = res = 0
        l3 = len(intersection)
        while p1 < l1 and p2 < l2 and cur < l3:
            if nums1[p1] < intersection[cur]:
                sum1 += nums1[p1]
                p1 += 1
            if nums2[p2] < intersection[cur]:
                sum2 += nums2[p2]
                p2 += 1
            
            # 两个指针都到了交汇点
            if nums1[p1] == intersection[cur] and nums2[p2] == intersection[cur]:
                res += max(sum1, sum2) + intersection[cur]
                sum1 = sum2 = 0
                p1 += 1
                p2 += 1
                cur += 1

        res += max(sum(nums1[p1:]), sum(nums2[p2:]))

        return res % (10 ** 9 + 7)


