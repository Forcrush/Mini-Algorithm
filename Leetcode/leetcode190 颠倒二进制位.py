# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-09 08:53:39
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-09 08:59:36


class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		return int(bin(n)[2:].zfill(32)[::-1], 2)