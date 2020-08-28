# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-15 23:01:44
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-16 00:24:35


class Solution:
	def scheduleCourse(self, courses):
		# 1 按照结束时间对课程进行排序
		# 2 使用一个大顶堆来储存已经选择的课程的长度
		# 3 一旦发现安排了当前课程之后，其结束时间超过了最晚结束时间，那么就从已经安排的课程中，取消掉一门最耗时的课程
		import heapq as hq
		courses.sort(key=lambda x:x[1])
		cur = 0
		selected_course = []
		for c in courses:
			hq.heappush(selected_course, -c[0])
			cur += c[0]
			if cur > c[1]:
				# 因为是小根堆存的负数 直接相加即可
				cur += hq.heappop(selected_course)
		return len(selected_course)
