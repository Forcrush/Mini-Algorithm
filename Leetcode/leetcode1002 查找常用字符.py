# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-26 14:27:22
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-26 14:35:22


class Solution:
	def commonChars(self, A):
		dic_res = {}
		for i in A[0]:
			dic_res[i] = dic_res.get(i, 0) + 1
		A.pop(0)

		for word in A:
			tmp = {}
			for cha in word:
				if cha in dic_res:
					tmp[cha] = min(tmp.get(cha, 0)+1, dic_res[cha])
			dic_res = tmp
		res = []
		for key,value in dic_res.items():
			res.extend([key]*value)
		return res

