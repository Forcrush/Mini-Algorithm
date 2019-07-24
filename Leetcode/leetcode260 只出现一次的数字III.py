# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-23 20:59:24
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-23 21:43:38


'''
先全部异或一次, 得到的结果, 考察其的某个非0位(比如最高非0位), 那么只出现一次的两个数中, 
在这个位上一个为0, 一个为1, 由此可以将数组中的元素分成两部分,重新遍历, 求两个异或值
'''
class Solution:
	def singleNumber(self, nums):
		eor = 0
		for i in nums:
			eor ^= i
		length = len(bin(eor)) - 2
		a, b = 0, 0
		for i in nums:
			if i >> (length-1) & 1:
				a ^= i
			else:
				b ^= i
		return [a, b]