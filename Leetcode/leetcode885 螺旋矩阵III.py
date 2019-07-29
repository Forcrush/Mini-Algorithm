# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-26 15:28:12
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-26 16:36:57


class Solution:
	def spiralMatrixIII(self, R, C, r0, c0):
		def inmatrix(r, c):
			if 0 <= r <= R-1 and 0 <= c <= C-1:
				return True
			else:
				return False
		count = 0
		colbegin, colend, rowbegin, rowend = c0, c0, r0, r0
		poslist = []

		while count < R*C:

			for i in range(colbegin, colend+1):
				if inmatrix(rowbegin, i):
					poslist.append([rowbegin, i])
					count += 1
			colend += 1

			for i in range(rowbegin, rowend+1):
				if inmatrix(i, colend):
					poslist.append([i, colend])
					count += 1
			rowend += 1

			for i in range(colend, colbegin-1, -1):
				if inmatrix(rowend, i):
					poslist.append([rowend, i])
					count += 1
			colbegin -= 1

			for i in range(rowend, rowbegin-1, -1):
				if inmatrix(i, colbegin):
					poslist.append([i, colbegin])
					count += 1
			rowbegin -= 1

		return poslist

