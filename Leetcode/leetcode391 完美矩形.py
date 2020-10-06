# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-17 11:44:02
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-17 11:57:11


# 总面积等于小块的面积和
# 如果是完美覆盖 除大矩形4个顶点外其它点都出现偶数(2或4)次
class Solution:
	def isRectangleCover(self, rectangles):
		# rectangles中每个元素: [left, bottom, right, top]
		from collections import defaultdict
		
		left, right, top, bottom = float('inf'), float('-inf'), float('-inf'), float('inf')
		area_sum = 0
		vertex = defaultdict(int)
		for r in rectangles:
			left = min(left, r[0])
			bottom = min(bottom, r[1])
			right = max(right, r[2])
			top = max(top, r[3])

			area_sum += abs(r[2]-r[0]) * abs(r[3]-r[1])
			vertex[(r[0], r[1])] += 1
			vertex[(r[2], r[3])] += 1
			vertex[(r[0], r[3])] += 1
			vertex[(r[2], r[1])] += 1

		if area_sum != abs(right-left) * abs(top-bottom):
			return False

		# 将大矩形四个顶点加入
		vertex[(left, bottom)] += 1
		vertex[(left, top)] += 1
		vertex[(right, bottom)] += 1
		vertex[(right, top)] += 1

		for k,v in vertex.items():
			if v % 2 != 0:
				return False
		return True
