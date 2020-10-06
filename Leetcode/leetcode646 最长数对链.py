# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-18 14:34:56
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-18 14:38:33


class Solution:
	def findLongestChain(self, pairs):
		pairs.sort(key=lambda x:x[0])

		dp = [1] * len(pairs)

		for i in range(1, len(pairs)):
			for j in range(i):
				if pairs[j][1] < pairs[i][0]:
					dp[i] = max(dp[i], dp[j]+1)

		return max(dp)

