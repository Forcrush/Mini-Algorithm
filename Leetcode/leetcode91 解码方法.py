# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-17 13:42:15
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-17 15:28:21


# 递归法
class Solution1:
	def numDecodings(self, s):
		self.res = 0

		def decode(start):
			if start >= len(s):
				self.res += 1
				return
			for i in range(start+1, len(s)+1):
				if int(s[start:i]) >= 1 and int(s[start:i]) <= 26:
					decode(i)
				else:
					return

		decode(0)
		return self.res


# 动态规划
class Solution2:
	def numDecodings(self, s):
		cnt = 0
		if len(s) == 0:
			return 0
		if len(s) == 1:
			if s[0] == '0':
				return 0
			else:
				return 1
		dp = [0] * (len(s) + 1)
		dp[0] = 1
		for i in range(0, len(s)):
			if s[i] == '0':
				dp[i+1] = 0
			else:
				dp[i+1] = dp[i]
			if i > 0:
				if s[i-1] == '1':
					dp[i+1] += dp[i-1]
				elif s[i-1] == '2' and s[i] <= '6':
					dp[i+1] += dp[i-1]

		return dp[len(s)]

