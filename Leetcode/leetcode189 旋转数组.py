# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-07 20:57:12
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-07 22:03:18


# 反转法
class Solution:
	def rotate(self, nums, k):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		k %= len(nums)
		# 反转整个字符串
		start, end = 0, len(nums)-1
		while start <= end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1
		# 反转字符串前半部分
		start, end = 0, k-1
		while start <= end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1
		# 反转字符串后半部分
		start, end = k, len(nums)-1
		while start <= end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1


# 环状替换法
class Solution2:
	def rotate(self, nums, k):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		k %= len(nums)
		count = 0
		start = 0
		while count < len(nums):
			startbackup = start
			cur = nums[start]
			while True:
				nextpos = (start + k) % len(nums)
				temp = nums[nextpos]
				nums[nextpos] = cur
				cur = temp
				start = nextpos
				count += 1
				if start == startbackup:
					break
			start += 1

		return nums
