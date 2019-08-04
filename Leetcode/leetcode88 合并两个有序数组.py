# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 14:39:39
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 14:52:28


class Solution:
	def merge(self, nums1, m, nums2, n):
		"""
		Do not return anything, modify nums1 in-place instead.
		"""
		point1 = m-1
		point2 = n-1
		end = m + n - 1
		while point1 >= 0 and point2 >= 0:
			if nums1[point1] >= nums2[point2]:
				nums1[end] = nums1[point1]
				end -= 1
				point1 -= 1
			else:
				nums1[end] = nums2[point2]
				end -= 1
				point2 -= 1
		while point1 >= 0:
			nums1[end] = nums1[point1]
			end -= 1
			point1 -= 1
		while point2 >= 0:
			nums1[end] = nums2[point2]
			end -= 1
			point2 -= 1

			