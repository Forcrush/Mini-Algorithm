# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 21:48:25
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 22:10:22


class Solution(object):
	def largestTriangleArea(self, points):
		res = 0
		for i in range(len(points)):
			for j in range(i+1, len(points)):
				for k in range(j+1, len(points)):
					res = max(abs((points[i][0] * points[j][1] - points[j][0] * points[i][1])\
								 + (points[j][0]*points[k][1] - points[k][0] * points[j][1])\
								 + (points[k][0] * points[i][1] - points[i][0]*points[k][1]))\
								 / 2.0, res)
		return res

		