# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-26 22:17:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-26 22:20:11


class Solution:
	def minMoves2(self, nums):

		nums.sort()

		mid = (len(nums) - 1) // 2
		res = 0
		for i in nums:
			res += abs(i - nums[mid])
			
		return res