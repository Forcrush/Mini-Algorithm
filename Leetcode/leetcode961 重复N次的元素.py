# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-24 13:15:01
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-24 13:23:11


class Solution:
	def repeatedNTimes(self, A):
		for i in range(len(A)-1):
			if A[i] == A[i+1]:
				return A[i]
		# 10121314
		if A[0] == A[2]:
			return A[0]
		# 01213141
		if A[1] == A[3]:
			return A[1]
		# 10213141
		if A[0] == A[-1]:
			return A[0]