# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-26 21:53:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-26 22:35:07


class Solution:
	def findClosestElements(self, arr, k, x):
		
		if k > len(arr): return []
		if x <= arr[0]: return arr[:k]
		if x >= arr[-1]: return arr[-k:]

		left, right = 0, len(arr)-1
		i, j = -1, -1
		while left < right:
			mid = (left + right) >> 1
			if arr[mid] == x:
				# x in array
				i, j = mid, mid+1
				break
			elif arr[mid] < x:
				left = mid + 1
			else:
				right = mid

		# left == right
		if i < 0 and j < 0:
			i, j = left-1, left

		# find k elements
		cnt = 0
		while True:
			if cnt == k:
				break
			if 0 <= i and j < len(arr):
				if abs(arr[i]-x) < abs(arr[j]-x):
					i -= 1
					cnt += 1
					continue
				elif  abs(arr[i]-x) > abs(arr[j]-x):
					j += 1
					cnt += 1
					continue
				else:
					i -= 1
					cnt += 1
					continue
			if i < 0:
				j += 1
				cnt += 1
				continue
			if j >= len(arr):
				i -= 1
				cnt += 1
				continue

		return arr[i+1:j]

