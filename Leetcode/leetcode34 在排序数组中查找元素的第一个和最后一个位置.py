# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-13 09:10:57
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-13 10:06:17


class Solution:
	def searchRange(self, nums, target):

		def find_left_pos(nums, target):
			beg, end = 0, len(nums)
			while beg < end:
				mid = beg + (end - beg) // 2
				# 收紧右边界
				if nums[mid] >= target:
					end = mid
				else:
					beg = mid + 1
			return beg

		def find_right_pos(nums, target):
			beg, end = 0, len(nums)
			while beg < end:
				mid = beg + (end - beg) // 2
				# 收紧左边界
				if nums[mid] <= target:
					beg = mid + 1
				else:
					end = mid
			return beg - 1

		left, right = find_left_pos(nums, target), find_right_pos(nums, target)
		if left == len(nums) or nums[left] != target:
			return [-1, -1]
		else:
			return [left, right]
			