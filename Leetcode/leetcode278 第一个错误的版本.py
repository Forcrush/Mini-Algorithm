# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 17:30:26
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-03 17:37:53


class Solution:
	def firstBadVersion(self, n):
		begin, end = 1, n
		while begin < end:
			mid = begin + (end - begin) // 2
			if isBadVersion(mid):
				end = mid
			else:
				begin = mid + 1
		return begin