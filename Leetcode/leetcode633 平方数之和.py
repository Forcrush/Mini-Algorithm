# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-16 16:04:41
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-16 17:01:03


class Solution:
	def judgeSquareSum(self, c):
		inferior = 0
		superior = int(c**0.5)
		
		while inferior <= superior:
			if inferior**2 + superior**2 == c:
				return True
			if inferior**2 + superior**2 < c:
				inferior += 1
			if inferior**2 + superior**2 > c:
				superior -= 1

		return False