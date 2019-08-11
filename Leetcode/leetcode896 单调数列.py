# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-11 19:47:00
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-11 19:59:44


class Solution:
	def isMonotonic(self, A):
		if len(A) < 3:
			return True
		increase, decrease = 0, 0
		for i in range(len(A)-1):
			if A[i] < A[i+1]:
				increase += 1
			elif A[i] > A[i+1]:
				decrease += 1
		if increase and decrease:
			return False
		return True

		