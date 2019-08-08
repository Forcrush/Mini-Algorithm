# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-08 20:06:51
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-08 20:17:44


# self-bitmap
class Solution:
	def findDisappearedNumbers(self, nums):
		if nums == [] or nums == [1]:
			return []
		for i in nums:
			i = abs(i)
			if i == len(nums):
				nums[0] = -abs(nums[0])
			else:
				nums[i] = -abs(nums[i])
		res = []
		for i in range(1, len(nums)):
			if nums[i] > 0:
				res.append(i)
		if nums[0] > 0:
			res.append(len(nums))
		return res

