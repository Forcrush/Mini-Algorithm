# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-12 21:07:58
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-12 21:51:44


# 01背包需装满问题
class Solution:
	def canPartition(self, nums):
		if nums == []:
			return True
		if len(nums) == 1:
			return False
		totalweight = sum(nums)
		if totalweight % 2 == 1:
			return False
		totalweight //= 2
		dp = [[0 for _ in range(totalweight+1)] for _ in range(len(nums)+1)]

		for i in range(1, len(nums)+1):
			for j in range(nums[i-1], totalweight+1):
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]] + nums[i-1])

		if dp[len(nums)][totalweight] == totalweight:
			return True
		else:
			return False