# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 13:42:21
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 14:51:50

、
# 对 C(n, k) 优化 -- C(n, k) == C(n, n-k)
class Solution:
	def combine(self, n, k):
		if k > n:
			return []

		array = [i+1 for i in range(n)]
		res = []

		def findcomb(comb, usenum, start, knum):
			if usenum == knum:
				res.append(comb + [])
				return
			if start > n-1:
				return
			findcomb(comb, usenum, start+1, knum)
			findcomb(comb+[array[start]], usenum+1, start+1, knum)

		if k > n//2:
			findcomb([], 0, 0, n-k)
			for i in range(len(res)):
				res[i] = list(set(array)-set(res[i]))
			return res
		else:
			findcomb([], 0, 0, k)
			return res

