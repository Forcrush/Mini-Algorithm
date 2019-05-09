# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 15:47:39
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-09 15:50:11


class Solution:
	def canJump(self, nums):
		if len(nums) == 0:
			return False
			
		maxjump = -1
		for i in range(0, len(nums)):
			if nums[i] > maxjump:
				maxjump = nums[i]
			if i+maxjump >= len(nums)-1:
				return True
			if maxjump == 0:
				return False
			maxjump -= 1

		return False