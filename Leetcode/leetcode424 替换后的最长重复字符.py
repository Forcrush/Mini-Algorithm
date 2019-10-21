# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-16 08:40:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-16 08:48:25


class Solution:
	def characterReplacement(self, s, k):
		start, end, dominant, res = 0, 0, 0, 0
		win_dic = {}
		while end < len(s):
			win_dic[s[end]] = win_dic.get(s[end], 0) + 1
			dominant = max(dominant, win_dic[s[end]])
			while end-start+1-dominant > k:
				win_dic[s[start]] -= 1
				start += 1
			res = max(res, end-start+1)
			end += 1
		return res