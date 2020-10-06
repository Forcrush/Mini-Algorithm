# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-17 16:38:10
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-17 16:51:27


class Solution:
	def maxRotateFunction(self, A):
		S, K = sum(A), len(A)-1
		res = float('-inf')
		pre = 0
		for i in range(len(A)):
			pre += i * A[i]
		res = max(res, pre)
		for i in range(1, len(A)):
			cur = pre + S - (K+1) * A[K+1-i]
			res = max(res, cur)
			pre = cur
		return res

		