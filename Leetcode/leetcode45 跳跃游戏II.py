# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 17:56:12
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-09 18:38:47


class Solution:
	def jump(self, nums):
		if len(nums) <= 1:
			return 0
		maxreach = nums[0]
		reach = 0
		step = 0
		for i in range(0, len(nums)):
			if i == maxreach and nums[i] == 0:
				return 0
			maxreach = max(maxreach, i+nums[i])
			if maxreach >= len(nums)-1:
				return step + 1
			if i == reach:
				step += 1
				reach = maxreach

		return step

