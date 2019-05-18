# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-15 18:45:07
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-15 18:57:08


class Solution:
	def combinationSum2(self, candidates, target):
		res = []
		candidates.sort()

		def findcomb(comb, start, cursum):
			if cursum == target:
				if comb not in res:
					res.append(comb + [])
				return

			if cursum > target or start > len(candidates)-1:
				return
			findcomb(comb + [candidates[start]], start + 1, cursum + candidates[start])
			findcomb(comb, start + 1, cursum)

		findcomb([], 0, 0)

		return res

t = [10,1,2,7,6,1,5]
print(Solution().combinationSum2(t,8))