# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 21:08:07
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 22:50:21


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


# 快速排序(随机选择)
# Time Complexity: O(n) -- 因为这个思想属于减治法 只需去解决一个分支
# 即期望的时间复杂度为 O(n) + O(n/2) + O(n/4) + O(n/8) + ... < 2*O(n) ~ O(n)
import random


class Solution2:
	def findKthLargest(self, nums, k):

		# ！！！
		# 存在分歧 即重复元素是否有效 若前k大元素中可以包含重复元素则不用去重 反之则需要
		# nums = list(set(nums))

		def random_divide(array, low, high):
			# 随机选取将要放置的数
			rand = random.randint(low, high)
			array[rand], array[low] = array[low], array[rand]

			tmp = array[low]
			while low != high:
				while low < high and array[high] > tmp:
					high -= 1
				if low < high:
					array[low] = array[high]
					low += 1
				while low < high and array[low] < tmp:
					low += 1
				if low < high:
					array[high] = array[low]
					high -= 1
			array[low] = tmp
			return low

		def quicksort(array, low, high):
			if low >= high:
				return 
			mid = random_divide(array, low, high)
			if mid == len(array) - k:
				return array[mid]
			elif mid > len(array) - k:
				return quicksort(array, low, mid-1)
			else:
				return quicksort(array, mid+1, high)

		quicksort(nums, 0, len(nums)-1)

		return nums[len(nums)-k]


# BFPRT算法
# Time Complexity: O(n)
class Solution3:
	def findKthLargest(self, nums, k):
		
