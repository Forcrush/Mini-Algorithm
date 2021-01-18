'''
Author: Puffrora
Date: 2021-01-17 15:49:45
LastModifiedBy: Puffrora
LastEditTime: 2021-01-18 11:20:15
'''


# DP
# 时间复杂度 O(N^2)
# 空间复杂度 O(N)
class Solution:
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        length = [0] * N
        count = [1] * N

        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] >= length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]

        longest = max(length)
        res = 0
        for i, c in enumerate(count):
            if length[i] == longest:
                res += c
        
        return res


# 线段树
# 时间复杂度 O(NlogN)
# 空间复杂度 O(N)

# ! To Be Continued...