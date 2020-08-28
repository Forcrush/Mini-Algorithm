# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-30 23:33:29
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-31 00:14:56


class Solution:
	def insert(self, intervals, newInterval):

		# intervals = []
		if not intervals:
			return [newInterval]

		# newInterval首元素比interval中第一个区间首元素更小 需提前加入
		if intervals[0][0] <= newInterval[0]:
			res = [intervals[0]]
			add_flag = False
		else:
			res = [newInterval]
			add_flag = True
		
		for i in range(len(intervals)):

			if intervals[i][0] >= newInterval[0] and not add_flag:
				
				if newInterval[0] > res[-1][-1]:
					res.append(newInterval)
				elif newInterval[-1] > res[-1][-1]:
					res[-1][-1] = newInterval[-1]
				add_flag = True

			if intervals[i][0] > res[-1][-1]:
				res.append(intervals[i])
			elif intervals[i][0] <= res[-1][-1] and intervals[i][-1] > res[-1][-1]:
				res[-1][-1] = intervals[i][-1]

		# 此时说明newInterval首元素比interval中所有区间首元素更大 需要再一次merge
		if not add_flag:
			if newInterval[0] > res[-1][-1]:
				res.append(newInterval)
			elif newInterval[-1] > res[-1][-1]:
				res[-1][-1] = newInterval[-1]

		return res

