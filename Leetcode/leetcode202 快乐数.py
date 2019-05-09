# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-06 22:21:35
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-06 22:51:37


class Solution:
	def isHappy(self, n):

		sqr = []

		def judge(n):
			if n == 1:
				return True
			s = str(n)
			nextnum = 0
			for i in s:
				nextnum += int(i) ** 2
			if nextnum == 1:
				return True
			if nextnum in sqr:
				return False
			else:
				sqr.append(nextnum)
				return judge(nextnum)

		return judge(n)

