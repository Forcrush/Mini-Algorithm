# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-21 20:43:11
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-21 22:18:00


# 时间复杂度 O(NlogN)
# 空间复杂度 O(N)
class Solution:
	def findRightInterval(self, intervals):

		for i in range(len(intervals)):
			intervals[i].append(i)

		# 按起点排序
		intervals.sort(key=lambda x:x[0])

		res = [-1] * len(intervals)
		for i in range(len(intervals)):
			# 二分查找
			l, r = i+1, len(intervals)-1
			if intervals[r][0] < intervals[i][1]:
				continue
			while l < r:
				mid = (l + r) // 2
				if intervals[mid][0] >= intervals[i][1]:
					r = mid
				else:
					l = mid + 1

			res[intervals[i][2]] = intervals[r][2]

		return res