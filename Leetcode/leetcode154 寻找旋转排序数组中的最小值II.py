# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 18:28:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 19:27:55


class Solution:
	def findMin(self, nums):

		def bi_find(left, right):

			if left == right:
				return nums[left]

			mid = (left + right) // 2

			# 前半部严格有序
			if nums[mid] > nums[left]:
				return min(nums[left], bi_find(mid+1, right))
			# 后半部严格有序
			elif nums[mid] < nums[right]:
				return min(nums[mid+1], bi_find(left, mid))
			# 两边都找
			else:
				return min(bi_find(left, mid), bi_find(mid+1, right))

		return bi_find(0, len(nums)-1)


# 非递归
class Solution:
	def findMin(self, nums):

		low, high = 0, len(nums) - 1

		while low < high:
			pivot = low + (high - low) // 2
			if nums[pivot] < nums[high]:
				high = pivot 
			elif nums[pivot] > nums[high]:
				low = pivot + 1
			else:
				high -= 1

		return nums[low]
