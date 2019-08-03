# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 20:03:24
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-03 20:26:11


class Solution:
	def findPoisonedDuration(self, timeSeries, duration):
		if timeSeries == []:
			return 0
		if len(timeSeries) == 1:
			return duration
		total = 0
		for i in range(1, len(timeSeries)):
			total += min(timeSeries[i]-timeSeries[i-1], duration)

		total += duration

		return total

'''
class Solution2:
	def findPoisonedDuration(self, timeSeries, duration):
		if timeSeries == []:
			return 0
		if len(timeSeries) == 1:
			return duration
		total, end = 0, 0
		for i in timeSeries:
			if i > end:
				total += duration
			else:
				total += duration - (end - i)
			end = i + duration

		return total
'''