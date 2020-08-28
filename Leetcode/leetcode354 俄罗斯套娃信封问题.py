# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-11 16:51:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-11 17:06:28

# 基数排序 + LIS算法(最长单增序列)
class Solution:
	def maxEnvelopes(self, envelopes):
		if not envelopes: return 0
		envelopes.sort(key=lambda x : (x[0], -x[1]))

		dp = [0] * len(envelopes)
		dp[0] = 1

		for i in range(1, len(envelopes)):
			m = 0
			for j in range(i):
				if dp[j] > m and envelopes[i][1] > envelopes[j][1]:
					m = dp[j]
			dp[i] = m + 1

		res = -1
		for i in dp:
			res = max(res, i)

		return res