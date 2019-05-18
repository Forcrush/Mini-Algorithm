# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-11 12:27:26
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-11 12:40:20


class Solution:
	def subsets(self, nums):
		res = []

		def findsubset(subset, length):
			if length == len(nums)+1:
				res.append(subset + [])
				return
			findsubset(subset, length + 1)
			findsubset(subset + [nums[length-1]], length + 1)
		findsubset([], 1)

		return res