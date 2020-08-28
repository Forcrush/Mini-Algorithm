# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-24 14:18:40
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-24 14:57:05


class Solution:
	def isAdditiveNumber(self, num):

		def satisfy(i, j, k):
			# 判断是否是 0xxx这种情况
			if (num[i] == '0' and j-i > 1) or (num[j] == '0' and k-j > 1):
				return False
			c = str(int(num[i:j]) + int(num[j:k]))
			# 判断第三个数是否是前两个数之和
			if c != num[k:k+len(c)]: return False
			# 判断是否到尾
			if k + len(c) == len(num): return True

			return satisfy(j, k, k+len(c))

		i = 0
		for j in range(i+1, len(num)-1):
			for k in range(j+1, len(num)):
				if satisfy(i, j, k):
					return True
		return False