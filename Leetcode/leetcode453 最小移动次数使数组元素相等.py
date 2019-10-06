# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 22:59:42
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 23:01:19


class Solution:
	def minMoves(self, nums):
		m = min(nums)
		res = 0
		for i in nums:
			res += i - m
		return res

		