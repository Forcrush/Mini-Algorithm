# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 18:28:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-12 11:58:41


class Solution:
	def findMin(self, nums):

		def bi_find(left, right):

			if left == right:
				return nums[left]

			mid = (left + right) // 2

			# 前半部有序
			if nums[mid] >= nums[left]:
				return min(nums[left], bi_find(mid+1, right))
			# 后半部有序
			else:
				return min(nums[mid+1], bi_find(left, mid))

		return bi_find(0, len(nums)-1)