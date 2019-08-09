# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-09 21:41:28
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 21:48:09


class Solution(object):
	def largestPerimeter(self, A):
		if len(A) < 3:
			return 0
		A.sort()
		for i in range(len(A)-3, -1, -1):
			if A[i] + A[i+1] > A[i+2]:
				return A[i] + A[i+1] + A[i+2]
		return 0