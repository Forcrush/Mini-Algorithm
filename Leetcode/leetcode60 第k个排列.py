# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-09 18:55:24
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-09 20:19:35


class Solution:
	def getPermutation(self, n, k):
		if n == 1:
			return '1'

		pool = [0,1,2,3,4,5,6,7,8,9]

		def factor(num):
			if num == 0:
				return 1
			else:
				res = 1
				while num >= 1:
					res *= num
					num -= 1
				return res

		seq = ''
		for i in range(1, n+1):
			if k % factor(n - i) == 0:
				num = k // factor(n - i)
			else:
				num = k // factor(n - i) + 1

			seq += str(pool[num])
			pool.pop(num)

			k -= k // factor(n - i) * factor(n - i)
			# 说明已找到第k个序列
			if k == 0:
				# 将剩下的数字逆序接上
				for i in range(len(pool)-1, 0, -1):
					if pool[i] <= n:
						seq += str(pool[i])
						pool.pop(i)
				return seq
