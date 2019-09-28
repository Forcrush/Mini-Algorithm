# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 22:27:18
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 22:49:57


class Solution:
	def findNthDigit(self, n):
		# 若flag_len = 3 表示此时在3位数区间 即100~999
		flag_len = 0
		sum_num = 0
		while sum_num < n:
			flag_len += 1
			sum_num += flag_len * 9 * (10 ** (flag_len-1))	
		# 目标数在flag_len位数区间
		dif = n - (sum_num - flag_len * 9 * (10 ** (flag_len-1)))
		quo = dif // flag_len
		rem = dif % flag_len
		if rem == 0:
			tar_num = str(int('1'+'0'*(flag_len-1)) + quo - 1)
			return int(tar_num[-1])
		else:
			tar_num = str(int('1'+'0'*(flag_len-1)) + quo)
			return int(tar_num[rem-1])

