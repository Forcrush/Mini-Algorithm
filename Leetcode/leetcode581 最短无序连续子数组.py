'''
Author: Puffrora
Date: 2020-10-10 22:40:16
LastModifiedBy: Puffrora
LastEditTime: 2020-10-10 22:48:55
'''


# 时间复杂度 O(N)
# 空间复杂度 O(1)
class Solution:
    def findUnsortedSubarray(self, nums):

        min_val, max_val = float('inf'), float('-inf')

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_val = min(min_val, nums[i])

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                max_val = max(max_val, nums[i])

        l, r = 0, 0
        for i in range(len(nums)):
            if nums[i] > min_val:
                l = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < max_val:
                r = i
                break
        
        if r - l > 0:
            return r - l + 1
        else:
            return 0

