# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 19:35:57
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 19:41:11


'''
使用dp数组，dp[i]代表组合数为i时使用nums中的数能组成的组合数的个数
dp[i] = dp[i-nums[0]] + dp[i-nums[1]] + dp[i=nums[2]] + ...
'''
class Solution:
	def combinationSum4(self, nums, target):
		dp = [0] * (target + 1)
		dp[0] = 1
		for i in range(1, target+1):
			for j in nums:
				if j <= i:
					dp[i] += dp[i-j]

		return dp[target]

		