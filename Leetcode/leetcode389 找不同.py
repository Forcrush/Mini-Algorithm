# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 18:35:43
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 18:37:54


class Solution:
	def findTheDifference(self, s, t):
		s_dic = {}
		for i in s:
			s_dic[i] = s_dic.get(i, 0) + 1
		for j in t:
			if j not in s_dic:
				return j
			s_dic[j] -= 1

		for key,val in s_dic.items():
			if val != 0:
				return key

				