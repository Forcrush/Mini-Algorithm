# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-10 19:03:01
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-11 02:00:24


'''
四种操作之后的结果，都可以看成是某个子串的不断重复
例如01010101可以看成只有前两位在重复，后边的几位是跟着他们变的，
而3k+1 确定的字串 1001001001，可以看成前三位在不断重复，取最大字串做为分析对象，
就是说前三位便能代表大于等于3个灯泡经过m次操作所能得到的所有状态
'''
class Solution:
	def flipLights(self, n, m):
		if n == 0 or m == 0:
			return 1
		if n == 1:
			return 2
		if n == 2:
			if m == 1:
				return 3
			else:
				return 4
		# n >= 3
		if m == 1:
			return 4
		if m == 2:
			return 7
		else:
			return 8

