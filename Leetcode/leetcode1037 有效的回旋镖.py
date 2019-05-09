# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-09 01:12:47
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-09 01:14:28


class Solution:
	def isBoomerang(self, points):
		# 若三点构成的三角形面积不为0 则满足题意
		a = (points[1][0] - points[0][0], points[1][1] - points[0][1])
		b = (points[2][0] - points[0][0], points[2][1] - points[0][1])
		alen = (a[0] ** 2 + a[1] ** 2) ** 0.5
		blen = (b[0] ** 2 + b[1] ** 2) ** 0.5
		if alen == 0 or blen == 0:
			return False
		print(a,b)
		cos = (a[0] * b[0] + a[1] * b[1]) / (alen * blen)
		sin = (1 - cos ** 2) ** 0.5
		print(cos,sin)
		# 精度损失弥补
		if sin < 1e-7:
			sin = 0
		area = 0.5 * alen * blen * sin
		if area == 0:
			return False
		else:
			return True