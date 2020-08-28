# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-22 18:07:45
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-22 18:17:27


# 0, 1 -> 
# 00, 01, 10, 11 -> 
# 100, 101, 110, 111 -> ...
class Solution:
	def countBits(self, num):

		dp = [0] * (num+1)

		base = 1
		while base <= num:
			for i in range(base, 2*base):

				dp[i] = dp[i-base] + 1
				if i == num:
					return dp

			base *= 2

		return dp

