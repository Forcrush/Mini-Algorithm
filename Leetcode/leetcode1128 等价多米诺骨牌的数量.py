# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-26 20:39:41
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-26 20:40:34


class Solution:
	def numEquivDominoPairs(self, dominoes):
		res = {}
		for i in dominoes:
			if i[0] > i[1]:
				res[str(i[1])+'+'+str(i[0])] = res.get(str(i[1])+'+'+str(i[0]), 0) + 1
			else:
				res[str(i[0])+'+'+str(i[1])] = res.get(str(i[0])+'+'+str(i[1]), 0) + 1
		
		num = 0
		for i in res.items():
			if i[1] > 1:
				num += i[1] * (i[1]-1) // 2

		return num