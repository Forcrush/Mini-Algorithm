# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-25 20:56:19
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-25 21:03:53


# Divide and Conquer
class Solution:
	def longestSubstring(self, s, k):
		if k > len(s): return 0
		rare_char = min(set(s), key=s.count)
		if s.count(rare_char) >= k:
			return len(s)
		return max(self.longestSubstring(seg, k) for seg in s.split(rare_char))