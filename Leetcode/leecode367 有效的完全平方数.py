# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-16 15:25:07
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-16 15:51:38

'''
An = (2n - 1)
Sn = n ^ 2
'''
class Solution:
	def isPerfectSquare(self, num):
		if num == 1:
			return True
		subtrahend = 1
		while True:
			if num < 0:
				return False
			if num == 0:
				return True
			num -= subtrahend
			subtrahend += 2