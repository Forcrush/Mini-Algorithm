# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 17:06:44
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 21:04:26


# 小根堆法(维持一个大小为k的最小堆 最后的堆顶元素即第k大元素)
# Time Complexity: O(k+(n-k)logk) ~ O(nlogk)
class Solution:
	def findKthLargest(self, nums, k):
		heap = [0] * k
		for i in range(k):
			heap[i] = nums[i]
		for i in range(len(heap)//2-1, -1, -1):
			self.percolate(heap, i, len(heap)-1)

		for j in range(k, len(nums)):
			if nums[j] > heap[0]:
				heap[0] = nums[j]
				self.percolate(heap, 0, len(heap)-1)

		return heap[0]


	def percolate(self, array, hole, end):
		tmp = array[hole]
		child = 2 * hole + 1
		while child <= end:
			if child < end and array[child] > array[child+1]:
				child += 1
			if array[child] < tmp:
				array[hole] = array[child]
				hole = child
				child = 2 * hole + 1
			else:
				break
		array[hole] = tmp

