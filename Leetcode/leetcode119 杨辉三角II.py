# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-07 23:32:34
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-07 23:42:19


# Space Complexity -- O(n)
class Solution:
	def getRow(self, rowIndex):
		res = [0] * (rowIndex + 1)
		res[0] = 1
		for j in range(1, rowIndex):
			res[j] = 1
			for i in range(j, 0, -1):
				res[i] = res[i] + res[i-1]
		res[rowIndex] = 1
		return res

