# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-20 09:23:58
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-21 12:31:11


class Solution:
	def countRangeSum(self, nums, lower, upper):
		if nums == []: return 0
		global res
		res = 0

		# arr is the prefix sum array
		arr = [0] * len(nums)
		arr[0] = nums[0]
		for i in range(1, len(arr)):
			arr[i] = nums[i] + arr[i-1]

		# In later process, we always check arr[j] - arr[i],
		# where j > i, which means the interval's length always > 1
		# so we need to consider when interval's length = 1 (i = j)
		for s in arr:
			if lower <= s <= upper:
				res += 1

		def merge(arr, left, mid, right):
			global res
			tmp = [0] * (right - left + 1)
			i, j, k = left, mid, 0

			# counting range
			low, high = mid, mid
			for lf in range(left, mid):
				while low <= right and arr[low] - arr[lf] < lower:
						low += 1
				while high <= right and arr[high] - arr[lf] <= upper:
						high += 1
				res += high - low

			# merge sort process
			while i < mid and j <= right:
				if arr[i] < arr[j]:
					tmp[k] = arr[i]
					i += 1
					k += 1
				else:
					tmp[k] = arr[j]
					j += 1
					k += 1
			while i < mid:
				tmp[k] = arr[i]
				i += 1
				k += 1
			while j <= right:
				tmp[k] = arr[j]
				j += 1
				k += 1
			for p in range(left, right+1):
				arr[p] = tmp[p-left]

		def mergesort(arr, left, right):
			if left == right:
				return
			mid = (left + right) // 2
			mergesort(arr, left, mid)
			mergesort(arr, mid+1, right)
			merge(arr, left, mid+1, right)


		mergesort(arr, 0, len(arr)-1)

		return res

