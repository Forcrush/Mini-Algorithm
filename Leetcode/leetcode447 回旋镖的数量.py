# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 22:36:42
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 22:50:19


class Solution:
	def numberOfBoomerangs(self, points):
		res = 0
		for i in range(len(points)):
			dic = {}
			for j in range(len(points)):
				dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
				dic[dis] = dic.get(dis, 0) + 1

			for key,val in dic.items():
				if val > 1:
					res += val * (val - 1)

		return res