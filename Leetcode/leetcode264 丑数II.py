# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-10 17:06:30
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 17:21:50


'''
假设我们现在已经有了一个丑数的有序数组，如果要找到下一个丑数，
则可以将数组中的每一个数乘以2，并将其中第一个大于当前丑数的的结果记为M2，
同样将当前有序数组每一个数都乘以3，第一个大于当前丑数的的结果记为M3，
同样方式得到乘以5的第一个大于当前丑数的结果记为M5，下一个丑数必然是min(M2, M3, M5)。
事实上我们并不必要将数组中的每个数都乘以2,3,5。对于乘以2来说，
我们只要找到第一个乘以2大于当前丑数的数在数组中的位置，同样找到第一个乘以3,5大于当前丑数的数的位置。
如果当前丑数记为M，然后就可以使用min(M*2, M*3, M*5)来产生下一个丑数。

'''
class Solution:
	def nthUglyNumber(self, n):
		# 三指针法 index[0]表示M2位置 index[1]表示M3位置 index[3]表示M5位置
		index = [0] * 3
		res = [1] * n
		for i in range(1, n):
			nextnum = min(res[index[0]] * 2, min(res[index[1]] * 3, res[index[2]] * 5))

			if nextnum == res[index[0]] * 2:
				index[0] += 1
			if nextnum == res[index[1]] * 3:
				index[1] += 1
			if nextnum == res[index[2]] * 5:
				index[2] += 1

			res[i] = nextnum

		return res[n-1]