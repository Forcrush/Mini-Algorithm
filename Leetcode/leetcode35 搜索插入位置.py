# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 17:11:29
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-03 17:24:52


class Solution:
	def searchInsert(self, nums, target):
		if nums == []:
			return 0
		begin, end = 0, len(nums)-1
		while begin <= end:
			mid = (begin + end) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				end = mid - 1
			else:
				begin = mid + 1
		return begin

