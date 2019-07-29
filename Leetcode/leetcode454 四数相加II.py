# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-29 19:49:32
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-29 20:08:24


class Solution:
	def fourSumCount(self, A, B, C, D):
		dic = {}
		res = 0
		for a in A:
			for b in B:
				dic[a+b] = dic.get(a+b, 0) + 1
		for c in C:
			for d in D:
				res += dic.get(-c-d, 0)
		return res