# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-03 16:50:09
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-03 17:11:12


class Solution:
	def findComplement(self, num):
		tmp = num
		digit = 0
		while tmp:
			tmp >>= 1
			digit <<= 1
			digit += 1
		return num ^ digit