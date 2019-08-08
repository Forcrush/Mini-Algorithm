# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-08 20:21:48
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-08 20:30:27


# self-bitmap
class Solution:
	def findDuplicates(self, nums):
		if nums == []:
			return []
		res = []
		for i in nums:
			i = abs(i)
			if i == len(nums):
				if nums[0] < 0:
					res.append(i)
				else:
					nums[0] = -nums[0]
			else:
				if nums[i] < 0:
					res.append(i)
				else:
					nums[i] = -nums[i]
		return res

		