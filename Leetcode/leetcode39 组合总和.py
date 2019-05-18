# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 15:01:25
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 19:25:08


class Solution:
	def combinationSum(self, candidates, target):
		res = []

		def findcomb(comb, start, cursum):
			if cursum == target:
				res.append(comb + [])
				return
			if cursum > target or start > len(candidates)-1:
				return
			findcomb(comb + [candidates[start]], start, cursum + candidates[start])
			findcomb(comb, start + 1, cursum)

		findcomb([], 0, 0)

		return res

