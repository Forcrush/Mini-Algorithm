# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-04 09:14:13
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-04 10:55:59


class Solution:
	def countAndSay(self, n):
		if n == 1:
			return '1'
		if n == 2:
			return '11'
		res = '11'
		for i in range(2, n):
			tmp = ''
			start, point = 0, 0
			while point < len(res)-1:
				if point == len(res) - 2:
					if res[point] == res[point+1]:
						tmp += str(point-start+2) + str(res[point])
					else:
						tmp += str(point-start+1) + str(res[point])
						tmp += '1' + str(res[point+1])
					break
				else:
					if res[point] == res[point+1]:
						point += 1
					else:
						tmp += str(point-start+1) + str(res[point])
						point += 1
						start = point
			res = tmp

		return res

