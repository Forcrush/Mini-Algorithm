# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 10:50:59
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 11:00:57


class Solution:
	def findMaxConsecutiveOnes(self, nums):		
		dp = [0] * len(nums)
		dp[0] = (1 if nums[0] else 0)
		for i in range(1, len(nums)):
			dp[i] = (dp[i-1]+1 if nums[i] else 0)

		dp2 = [0] * len(nums)
		dp2[0] = (1 if dp[0] else 0)
		res = dp2[0]
		for i in range(1, len(nums)):
			dp2[i] = (dp2[i-1]+1 if nums[i] else dp[i-1]+1)
			res = max(res, dp2[i])
		return res

