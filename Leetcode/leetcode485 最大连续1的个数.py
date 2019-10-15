# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-14 10:47:18
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-14 10:50:26


class Solution:
	def findMaxConsecutiveOnes(self, nums):
		res, tmp = 0, 0
		for i in nums:
			tmp += (1 if i else -tmp)
			res = max(res, tmp)
		return res
