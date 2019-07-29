# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-26 15:00:25
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-26 15:21:45


class Solution:
	def findErrorNums(self, nums):
		eor = 0
		for i in range(len(nums)):
			eor ^= nums[i]
			eor ^= i + 1
		length = len(bin(eor)) - 2

		a, b = 0, 0
		for i in range(len(nums)):
			if nums[i] >> (length-1) & 1:
				a ^= nums[i]
			else:
				b ^= nums[i]
			if (i+1) >> (length-1) & 1:
				a ^= i + 1
			else:
				b ^= i + 1

		for i in nums:
			if a == i:
				return [a, b]
			if b == i:
				return [b, a]