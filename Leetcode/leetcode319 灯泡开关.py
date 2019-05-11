# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-10 17:41:04
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 19:02:01


'''
第i个灯泡亮或不亮取决于i的因子个数：
12 --> 1 2 3 4 6 12
若因子个数为偶数则不亮 为奇数则亮

因此只有平方数的因子数为奇数
即计算i以内的平方数个数
'''
class Solution:
	def bulbSwitch(self, n):
		return int(n ** 0.5)