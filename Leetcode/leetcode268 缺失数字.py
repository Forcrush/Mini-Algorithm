# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-27 16:31:25
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-27 16:36:14


class Solution:
	def missingNumber(self, nums):
		res = 0
		for i in range(len(nums)):
			res ^= nums[i]
			res ^= i

		return res ^ len(nums)

		