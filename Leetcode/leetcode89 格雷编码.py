# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-31 12:34:05
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-31 12:47:55



'''
假设已经知道了 n 位格雷编码 Gray(n)，通过以下操作，可构造出 Gray(n+1)
1. n位格雷码 Gray(n): [G1, G2, G3, ..., G2^n]
2. 反转: [G2^n, ..., G3, G2, G1]
3. 最高位加1 Gray'(n): [G2^n+2^n, ..., G3+2^n, G2+2^n, G1+2^n]
4. 拼接: Gray(n+1) = Gray(n) + Gray'(n)
'''
class Solution:
	def grayCode(self, n):
		if n == 0: return [0]
		codes = self.grayCode(n-1)
		return codes + [ (1 << (n-1)) | x for x in codes[::-1]]

