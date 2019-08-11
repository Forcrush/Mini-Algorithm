# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 19:59:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 20:03:55


class Solution:
	def matrixReshape(self, nums, r, c):
		if r * c != len(nums) * len(nums[0]):
			return nums
		pool = []
		res = []
		for i in range(len(nums)):
			for j in range(len(nums[0])):
				pool.append(nums[i][j])
		for i in range(0, len(pool), c):
			res.append(pool[i:i+c])
		return res

        