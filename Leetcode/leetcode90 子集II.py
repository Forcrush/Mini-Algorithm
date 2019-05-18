# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-12 18:20:02
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-12 21:07:22


class Solution:
	def subsetsWithDup(self, nums):
		res = []

		# 桶排序对原数组排序
		minval, maxval = nums[0], nums[0]
		for i in nums:
			minval = min(minval, i)
			maxval = max(maxval, i)
		tmp = [0] * (maxval - minval + 1)
		for i in nums:
			tmp[i-minval] += 1
		newnum = []
		for i in range(len(tmp)):
			newnum += [i+minval] * tmp[i]

		def findsubset(subset, length):
			if length == len(nums)+1:
				if subset not in res:
					res.append(subset + [])
				return
			findsubset(subset, length + 1)
			findsubset(subset + [nums[length-1]], length + 1)
		findsubset([], 1)

		return res