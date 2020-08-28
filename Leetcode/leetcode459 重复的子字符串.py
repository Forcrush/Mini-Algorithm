# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-02-14 10:56:33
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-02-14 11:27:58


# KMP
# 若 S 是由 N 个重复子串 s 构成 -> Ns
# 则 KMP 匹配出来的最长前后缀必为 (N-1)个s构成的子串
class Solution:
	def repeatedSubstringPattern(self, s):
		if len(s) < 2: return False
		next = [-1] * len(s)
		k = -1
		for q in range(1, len(s)):
			while k > -1 and s[q] != s[k+1]:
				k = next[k]
			if s[q] == s[k+1]:
				k += 1
			next[q] = k
		maxPreSuffixLen = next[len(s)-1] + 1

		return True if maxPreSuffixLen and len(s) % (len(s) - maxPreSuffixLen) == 0 else False


# 假设母串 S 是由子串 s 重复 N 次而成
# 则 S+S 则有子串 s 重复 2N 次
# 现在 S=Ns, S+S=2Ns, 因此 S 在 (S+S)[1:-1] 中必出现一次以上
class Solution2:
	def repeatedSubstringPattern(self, s):
		return s in (s+s)[1:-1]

		