# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 21:56:00
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 22:13:35


class Solution:
	def addToArrayForm(self, A, K):
		K = str(K)
		i, j = len(A)-1, len(K)-1
		carry = 0
		res = []

		while i >= 0 and j >= 0:
			tmp = A[i] + int(K[j]) + carry
			carry = tmp // 10
			res.append(tmp % 10)
			i -= 1
			j -= 1

		while i >= 0:
			tmp = A[i] + carry
			carry = tmp // 10
			res.append(tmp % 10)
			i -= 1

		while j >= 0:
			tmp = int(K[j]) + carry
			carry = tmp // 10
			res.append(tmp % 10)
			j -= 1
			
		if carry:
			res.append(carry)

		return res[::-1]

