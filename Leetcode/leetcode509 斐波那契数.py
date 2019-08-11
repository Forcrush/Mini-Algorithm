# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 19:38:11
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 19:43:45


class Solution:
	def fib(self, N):
		if N == 0:
			return 0
		if N == 1:
			return 1
		a, b = 0, 1
		for _ in range(N-1):
			b = a + b
			a = b - a
		return b

		