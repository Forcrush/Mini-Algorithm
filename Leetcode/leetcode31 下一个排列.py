# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-09 18:44:27
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-09 18:52:48


class Solution:
	def nextPermutation(self, nums):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		if nums == []:
			return
		if len(nums) == 1:
			return

		# 寻找第一个非递增数 如没有则说明已到最大序列
		for i in range(len(nums)-2, -1, -1):
			if nums[i] < nums[i+1]:
				nonincrease = i
				break
			# 逆序排列即得到最小序列
			if i == 0:
				lb = 0
				rb = len(nums) - 1
				while lb < rb:
					nums[lb], nums[rb] = nums[rb], nums[lb]
					lb += 1
					rb -= 1
				return

		# 在[nonincrease+1, len(nums)-1]中寻找最小的大于nums[nonincrease]的数 若存在多个相同的此数则取序列中最后一个
		# 因为nums[nonincrease + 1] > nums[nonincrease]
		minpos = nonincrease + 1
		for i in range(nonincrease+1, len(nums)):
			if nums[i] > nums[nonincrease]:
				if nums[i] <= nums[minpos]:
					minpos = i
		nums[nonincrease], nums[minpos] = nums[minpos], nums[nonincrease]

		# 对num[nonincrease+1, len(nums)-1]逆序排列
		lb = nonincrease + 1
		rb = len(nums) - 1
		while lb < rb:
			nums[lb], nums[rb] = nums[rb], nums[lb]
			lb += 1
			rb -= 1

