# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-17 20:55:04
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-17 21:05:53


class Solution:
	def sortColors(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		zeropos = 0
		twopos = len(nums) - 1
		point = 0
		while point <= twopos:
			if nums[point] == 0:
				nums[point], nums[zeropos] = nums[zeropos], nums[point]
				zeropos += 1
				point += 1
			elif nums[point] == 2:
				nums[point], nums[twopos] = nums[twopos], nums[point]
				twopos -= 1
			else:
				point += 1

