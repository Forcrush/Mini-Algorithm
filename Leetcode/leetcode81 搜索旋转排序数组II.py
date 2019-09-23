# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-23 10:22:53
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-23 10:33:56


class Solution:
	def search(self, nums, target):
		if nums == []:
			return False
		start, end = 0, len(nums)-1
		while start <= end:
			mid = start + (end - start) // 2
			if nums[mid] == target:
				return True
			if nums[mid] == nums[start]:
				start += 1
				continue
			# 前半部分有序
			if nums[start] < nums[mid]:
				# 在前半部分
				if nums[mid] > target and target >= nums[start]:
					end = mid - 1
				# 在后半部分
				else:
					start = mid + 1
			# 后半部分有序
			else:
				# 在后半部分
				if nums[mid] < target and target <= nums[end]:
					start = mid + 1
				# 在前半部分
				else:
					end = mid - 1
		return False

		