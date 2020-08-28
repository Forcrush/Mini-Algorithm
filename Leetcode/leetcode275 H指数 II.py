# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 18:16:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-17 18:23:18


# 因为是有序的 跟 y=x 这条直线比较
# 时间复杂度 O(n)
# 空间复杂度 O(1)
class Solution:
	def hIndex(self, citations):

		for i in range(len(citations)-1, -1, -1):
			j = len(citations) - i
			if citations[i] < j:
				return j - 1

		return len(citations)


# 二分搜索
# 时间复杂度 O(logn)
# 空间复杂度 O(1)
class Solution:
	def hIndex(self, citations):

		n = len(citations)
		left, right = 0, n - 1

		while left <= right:
			mid = left + (right - left) // 2
			if citations[mid] == n - mid:
				return n - mid
			elif citations[mid] < n - mid:
				left = mid + 1
			else:
				right = mid - 1
		
		return n - left

