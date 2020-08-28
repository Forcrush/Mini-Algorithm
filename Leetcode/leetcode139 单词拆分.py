# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 11:07:19
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 11:20:32


# DP
# dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0:i-1] 是否能被空格拆分成若干个字典中出现的单词
# dp[i] = dp[j] && (s[j:i] in Dic)
# dp[0] = True 表示空串情况成立
class Solution:
	def wordBreak(self, s, wordDict):
		dic_set = set()
		for w in wordDict:
			dic_set.add(w)
		dp = [False] * (len(s) + 1)
		dp[0] = True
		for i in range(1, len(s)+1):
			for j in range(i):
				if dp[j] and s[j:i] in dic_set:
					dp[i] = True
					break

		return dp[-1]