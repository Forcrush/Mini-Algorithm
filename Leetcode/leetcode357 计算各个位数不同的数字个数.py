# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-24 15:34:38
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-24 15:41:31


class Solution:
	def countNumbersWithUniqueDigits(self, n):
		# 0 是特殊情况
		if n == 0: return 1
		if n == 1: return 10
		'''
		* 排列组合：n位有效数字 = 每一位都从 0~9 中选择，且不能以 0 开头
		* 1位数字：0~9                      10
		* 2位数字：C10-2，且第一位不能是0      9 * 9
		* 3位数字：C10-3，且第一位不能是0      9 * 9 * 8
		* 4位数字：C10-4，且第一位不能是0      9 * 9 * 8 * 7
		* ... ...
		* 最后，总数 = 所有 小于 n 的位数个数相加
		'''
		cnt = 11
		tmp = 81
		for i in range(2, min(n, 10)+1):
			cnt += tmp
			tmp *= (10 - i)
		return cnt