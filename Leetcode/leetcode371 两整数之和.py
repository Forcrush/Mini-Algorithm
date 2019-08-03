# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-08-01 10:51:51
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-08-01 16:22:38


'''
在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，
这就需要我们手动对 Python 中的整数进行处理，手动模拟 32 位 INT 整型。

具体做法是将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0。
'''
class Solution:
	def getSum(self, a, b):
		# 2^32
		MASK = 0x100000000
		# 整型最大值
		MAX_INT = 0x7FFFFFFF
		MIN_INT = MAX_INT + 1
		while b != 0:
			# 计算进位
			carry = (a & b) << 1 
			# 取余范围限制在 [0, 2^32-1] 范围内
			a = (a ^ b) % MASK
			b = carry % MASK
		return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

