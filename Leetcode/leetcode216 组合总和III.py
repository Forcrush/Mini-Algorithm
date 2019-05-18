# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 19:02:59
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 19:18:24


class Solution:
	def combinationSum3(self, k, n):
		# range of k
		if k < 1 or k > 9:
			return []

		# range of n
		if n < (k+1)*k/2 or n > (19-k)*k/2:
			return []

		array = [i+1 for i in range(9)]
		res = []

		def findcomb(comb, start, cursum, usenum):
			if cursum == n and usenum == k:
				res.append(comb+[])
				return
			if start > 8 or cursum > n or usenum > k:
				return
			findcomb(comb, start+1, cursum, usenum)
			findcomb(comb+[array[start]], start+1, cursum+array[start], usenum+1)

		findcomb([], 0, 0, 0)
		return res

