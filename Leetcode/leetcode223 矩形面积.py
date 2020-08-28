# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-03 13:11:35
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-03 13:20:43


"""
输入参数为两个矩阵的左下和右上顶点坐标
					(C,D)/(G,H)
---------------------
|					|
|					|
|					|
---------------------
(A,B)/(E,F)
"""
class Solution:
	def computeArea(self, A, B, C, D, E, F, G, H):

		# 让第一个矩阵排在最左边
		if A > E:
			return self.computeArea(E, F, G, H, A, B, C, D)

		# 无重叠
		if C <= E or D <= F or B >= H:
			return abs(A-C) * abs(B-D) + abs(E-G) * abs(H-F)

		# 有重叠
		left = max(A, E)
		right = min(C, G)
		up = min(D, H)
		down = max(B, F)

		overlap = abs(left-right) * abs(up-down)

		return abs(A-C) * abs(B-D) + abs(E-G) * abs(H-F) - overlap