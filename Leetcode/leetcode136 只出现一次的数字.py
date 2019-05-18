# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-14 18:45:27
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-14 18:47:34


class Solution:
	def singleNumber(self, nums):
		res = nums[0]
		for i in range(1, len(nums)):
			res ^= nums[i]
		return res