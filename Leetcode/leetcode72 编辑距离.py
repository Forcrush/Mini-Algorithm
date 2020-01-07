# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-16 16:13:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-16 16:25:40


class Solution:
	def minDistance(self, word1, word2):
		dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

		match, delete, insert, replace = 0, 1, 1, 1
		for i in range(1, len(word1)+1):
			dp[0][i] = i
		for j in range(1, len(word2)+1):
			dp[j][0] = j

		for i in range(1, len(word2)+1):
			for j in range(1, len(word1)+1):
				if word2[i-1] == word1[j-1]:
					dp[i][j] = dp[i-1][j-1] + match
				else:
					dp[i][j] = min(dp[i-1][j]+insert, dp[i][j-1]+delete, dp[i-1][j-1]+replace)

		return dp[len(word2)][len(word1)]

a=""
b=""
print(Solution().minDistance(a,b))