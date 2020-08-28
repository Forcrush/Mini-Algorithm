# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-06 23:23:21
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-06 23:24:06


# DP
# 时间复杂度 O(n^2)
# 空间复杂度 O(n)
class Solution:
    def lengthOfLIS(self, nums):

        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        # print(dp)
        return max(dp)


# 贪心 + 二分
# 时间复杂度 O(nlogn)
# 空间复杂度 O(n)
class Solution2:
    def lengthOfLIS(self, nums):

        dp = []
        for n in nums:
            if not dp or n > dp[-1]:
                dp.append(n)

            # 找到第一个大于n的数并替换掉它
            else:
                left, right = 0, len(dp)-1
                loc = right
                while left <= right:
                    mid = (left + right) // 2
                    if dp[mid] >= n:
                        loc = mid
                        right -= 1
                    else:
                        left += 1

                dp[loc] = n

        # 此时dp为LIS
        return len(dp)

        