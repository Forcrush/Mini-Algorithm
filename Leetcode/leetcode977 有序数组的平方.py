# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 14:52:41
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 15:12:38


class Solution:
	def sortedSquares(self, A):
		mid, gap = 0, max(abs(A[0]), abs(A[-1]))+1
		for i in range(len(A)):
			if abs(A[i]) < gap:
				mid = i
				gap = abs(A[i])

		left, right = mid-1, mid+1
		res = [A[mid]**2]
		while left > -1 and right < len(A):
			if abs(A[left]) < abs(A[right]):
				res.append(A[left]**2)
				left -= 1
			else:
				res.append(A[right]**2)
				right += 1
		while left > -1:
			res.append(A[left]**2)
			left -= 1
		while right < len(A):
			res.append(A[right]**2)
			right += 1

		return res

		