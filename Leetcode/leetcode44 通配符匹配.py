# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-01 12:00:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-01 12:29:32


'''
s 可能为空，且只包含从 a-z 的小写字母
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *
'?' 可以匹配任何单个字符
'*' 可以匹配任意字符串（包括空字符串）
'''
class Solution:
	def isMatch(self, s, p):

		dp = [[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]

		# s = "" and p = ""
		dp[0][0] = True

		for i in range(1, len(p)+1):
			if p[i-1] == '*':
				dp[i][0] = True
			else:
				break

		for i in range(1, len(p)+1):
			for j in range(1, len(s)+1):
				if p[i-1] == '*':
					dp[i][j] =  dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
				elif p[i-1] == '?':
					dp[i][j] = dp[i-1][j-1]
				else:
					if p[i-1] == s[j-1] and dp[i-1][j-1]:
						dp[i][j] = True

		return dp[len(p)][len(s)]

		