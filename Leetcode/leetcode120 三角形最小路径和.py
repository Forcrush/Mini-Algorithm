# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-08 13:30:09
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-08 13:38:00


# need no extra sapce
class Solution:
	def minimumTotal(self, triangle):
		if sum(triangle, []) == []:
			return 0
		for i in range(len(triangle)-2, -1, -1):
			# len(triangle[i]) == i + 1
			for j in range(i+1):
				triangle[-1][j] = min(triangle[-1][j] + triangle[i][j], triangle[-1][j+1] + triangle[i][j])
		
		return triangle[-1][0]
