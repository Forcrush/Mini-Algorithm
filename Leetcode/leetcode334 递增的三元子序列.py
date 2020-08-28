# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-14 15:41:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-14 15:45:54


class Solution:
	def increasingTriplet(self, nums):
		if len(nums) < 3:
			return False

		small, mid = float("Inf"), float("Inf")
		for i in nums:
			if i <= small:
				small = i
			elif i <= mid:
				mid = i
			else:
				return True
		return False
		