# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 23:11:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 23:28:55


class Solution:
	def readBinaryWatch(self, num):

		def count1(n):
			res = 0
			while n != 0:
				n &= n - 1
				res += 1
			return res

		res = []

		for i in range(0, 12):
			for j in range(0, 60):
				if count1(i) + count1(j) == num:
					res.append(str(i) + ':' + str(j) if j >= 10 else str(i) + ':' + '0' + str(j))

		return res

		