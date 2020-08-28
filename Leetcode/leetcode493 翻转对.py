# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-16 19:35:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 21:07:36


class Solution:
	def reversePairs(self, nums):

		if not nums: return 0
		global res
		res = 0
		def merge(arr, left, mid, right):
			global res

			# 寻找重要逆序对
			i, j = left, mid
			while i < mid and j <= right:
				if nums[i] > 2 * nums[j]:
					res += mid - i
					j += 1
				else:
					i += 1

			# 归并
			i, j, p = left, mid, 0
			tmp = [0] * (right-left+1)
			while i < mid and j <= right:
				if arr[i] >= arr[j]:
					tmp[p] = arr[j]
					j += 1
					p += 1				
				else:
					tmp[p] = arr[i]
					i += 1
					p += 1
			while i < mid:
				tmp[p] = arr[i]
				i += 1
				p += 1
			while j <= right:
				tmp[p] = arr[j]
				j += 1
				p += 1
			for t in range(len(tmp)):
				arr[left+t] = tmp[t]


		def merge_sort(arr, left, right):
			if left >= right:
				return
			mid = (left + right) // 2
			merge_sort(arr, left, mid)
			merge_sort(arr, mid+1, right)
			merge(arr, left, mid+1, right)

		merge_sort(nums, 0, len(nums)-1)
		return res


'''		
c = [-9,-5]
print(Solution().reversePairs(b))
'''