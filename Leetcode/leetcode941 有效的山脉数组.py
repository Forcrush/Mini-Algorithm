# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-04-14 17:12:29
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-04-14 17:19:09


class Solution:
	def validMountainArray(self, A):
		if len(A) < 3: return False
		if A[1] <= A[0]: return False
		get_peak = False
		for i in range(1, len(A)):
			if A[i] == A[i-1]: return False
			if not get_peak and A[i] < A[i-1]:
				get_peak = True
			if get_peak and A[i] > A[i-1]:
				return False
		return True if get_peak else False

