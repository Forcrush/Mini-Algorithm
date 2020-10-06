# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-19 16:12:24
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-19 16:26:44


# 贪心算法
# 时间复杂度 O(NlogN) --  线性遍历 O(N)  + 数组排序 O(NlogN)
# 空间复杂度 O(1)
class Solution:
	def eraseOverlapIntervals(self, intervals):

		if not intervals: return 0

		intervals.sort(key=lambda x:(x[0], x[1]))

		pre = intervals[0]
		res = 0

		for i in range(1, len(intervals)):
			if intervals[i][0] >= pre[1]:
				pre = intervals[i]
			else:
				if intervals[i][1] < pre[1]:
					pre = intervals[i]
				res += 1

		return res

