'''
Author: Puffrora
Date: 2020-10-13 12:29:43
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 13:10:26
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        
        if not nums or k <= 1: return 0

        left, right = 0, 0
        res = 0
        cur = 1
        while right < len(nums):
            cur *= nums[right]
            while cur >= k:
                cur /= nums[left]
                left += 1
            res += right - left + 1
            right += 1
        
        return res
