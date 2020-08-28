# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-11 18:19:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-11 18:52:34


class Solution:
	def maxTurbulenceSize(self, A):

		if len(A) == 1: return 1
		sign = []
		for i in range(1, len(A)):
			if A[i] > A[i-1]:
				# 1 代表大于号
				sign.append(1)
			elif A[i] < A[i-1]:
				# -1 代表小于号
				sign.append(-1)
			else:
				# 0代表等号
				sign.append(0)

		res, tmp = 0, 0 if sign[0] == 0 else 1
		for j in range(1, len(sign)):
			if sign[j] == 0:
				res = max(res, tmp)
				tmp = 0
				continue
			elif sign[j] == sign[j-1]:
				res = max(res, tmp)
				tmp = 1
				continue
			else:
				tmp += 1

		# can match to the end
		res = max(res, tmp)

		# res为 匹配到的交叉的大小与号数量的最大值

		return res + 1
		