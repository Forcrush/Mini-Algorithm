# -*- coding: utf-8 -*-
# @Author: Hongyu Chen
# @Date:   2019-05-10 14:41:07
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 14:48:03


class Solution:
	def isUgly(self, num):
		factor = [2, 3, 5]
		if num <= 0:
			return False
		if num == 1:
			return True
		while num > 1:
			copy = num
			for i in factor:
				if num % i == 0:
					num /= i
			if num == copy:
				return False
		return True
