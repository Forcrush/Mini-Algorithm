# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-07 00:08:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-07 00:23:08


class Solution:
	def longestConsecutive(self, nums):
		res = 0
		numset = set(nums)

		for num in nums:
			if num-1 not in numset:
				length = 1
				cur = num
				while (cur := cur+1) in numset:
					length += 1

				res = max(res, length)

		return res