# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-07-23 20:41:24
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-07-23 20:45:34

'''
0 ^ x = x

x ^ x = 0

x & ~x = 0

x & ~0 = x

一开始 a = 0, b = 0

x第一次出现 a = x, b = 0

x第二次出现 a = 0, b = x

x第三次出现 a = 0, b = 0

只出现一次的数，按照上面 x 第一次出现的规律可知 a = x, b = 0, 因此最后返回a
'''
class Solution:
	def singleNumber(self, nums):
		a, b = 0, 0
		for i in nums:
			a = (a ^ i) & ~b
			b = (b ^ i) & ~a
		return a