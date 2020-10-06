# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-10-05 20:36:13
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-10-05 20:41:03


# details: https://leetcode.com/problems/strange-printer/discuss/106795/Python-Straightforward-DP-with-Explanation
class Solution:
	def strangePrinter(self, s):

		# dp(i, j) be the number of turns needed to print s[i:j+1]
		def recur_dp(i, j):
			if i > j: return 0
			if (i, j) not in memo: 
				res = recur_dp(i+1, j) + 1
				for k in range(i+1, j+1):
					if s[k] == s[i]:
						res = min(res, recur_dp(i, k-1) + recur_dp(k+1, j))
				memo[(i, j)] = res

			return memo[(i, j)]

		memo = {}

		return recur_dp(0, len(s)-1)