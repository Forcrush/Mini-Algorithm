# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-10-26 09:20:08
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-10-26 10:09:22


class Solution:
	def merge(self, intervals):
		intervals.sort(key=lambda x:x[0])
		if len(intervals) == 0:
			return []
		start, end = 0, 0
		point = 0
		res = []
		while True:
			if end >= len(intervals)-1:
				break
			if intervals[end][-1] >= intervals[end+1][0] and intervals[end][-1] <= intervals[end+1][-1]:
				end += 1
			elif intervals[end][-1] >= intervals[end+1][0] and intervals[end][-1] > intervals[end+1][-1]:
				intervals.pop(end+1)
			elif intervals[end][-1] < intervals[end+1][0]:
				res.append([intervals[start][0], intervals[end][-1]])
				start, end = end+1, end+1

		res.append([intervals[start][0], intervals[end][-1]])

		return res

