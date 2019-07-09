# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-27 13:59:27
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-27 14:03:08


class Solution:
	def hammingDistance(self, x, y):
		n = x ^ y
		n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
		n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
		n = (n & 0x0F0F0F0F) + ((n >> 4) & 0x0F0F0F0F)
		n = (n & 0x00FF00FF) + ((n >> 8) & 0x00FF00FF)
		n = (n & 0x0000FFFF) + ((n >> 16) & 0x0000FFFF)
		
		return n