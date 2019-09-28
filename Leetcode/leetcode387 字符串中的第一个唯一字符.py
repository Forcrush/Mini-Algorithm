# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 18:30:50
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 18:34:49


class Solution:
	def firstUniqChar(self, s):
		s_dic = {}
		for i in s:
			s_dic[i] = s_dic.get(i, 0) + 1
		print(s_dic)
		for i in range(len(s)):
			if s_dic[s[i]] == 1:
				return i

		return -1

		