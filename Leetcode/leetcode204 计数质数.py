# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-08-09 21:22:14
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-08-09 21:34:31


'''
埃拉托斯特尼筛法(sieve of Eratosthenes)
'''
class Solution(object):
	def countPrimes(self, n):
		if n == 1:
			return 0
		count = 0
		flag = [True] * n
		for i in range(2, n):
			if flag[i] == True:
				count += 1
				for j in range(i, n, i):
					flag[j] = False
		return count