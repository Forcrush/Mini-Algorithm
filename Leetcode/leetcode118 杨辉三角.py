# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-07 23:42:53
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-07 23:52:03


class Solution:
	def generate(self, numRows):
		if numRows == 0:
			return []
		if numRows == 1:
			return [[1]]
		if numRows == 2:
			return [[1], [1, 1]]
		res = [[1], [1, 1]]
		for _ in range(2, numRows):
			top = res[-1]
			tmp = [1]
			for i in range(len(top)-1):
				tmp.append(top[i] + top[i+1])
			tmp.append(1)
			res.append(tmp)
		return res

