# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-26 20:40:48
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-26 20:55:03


# heapq 可以插入一个数组 key默认为数组第一个元素
class Solution:
	def kSmallestPairs(self, nums1, nums2, k):
		import heapq as hq

		heap = []
		res = []
		def push(i, j):
			if i < len(nums1) and j < len(nums2):
				hq.heappush(heap, [nums1[i]+nums2[j], i, j])

		push(0, 0)
		while heap and len(res) < k:
			_, i, j = hq.heappop(heap)
			res.append([nums1[i], nums2[j]])
			push(i, j+1)
			if j == 0:
				push(i+1, 0)

		return res