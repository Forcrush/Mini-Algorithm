# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-10 17:22:09
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 17:40:47


class Solution:
	def nthSuperUglyNumber(self, n, primes):
		index = [0] * len(primes)
		res = [1] * n
		for i in range(1, n):
			nextnum = res[index[0]] * primes[0]
			for j in range(1, len(index)):
				nextnum = min(nextnum, res[index[j]] * primes[j])

			for k in range(len(index)):
				if nextnum == res[index[k]] * primes[k]:
					index[k] += 1

			res[i] = nextnum

		return res[n-1]

		