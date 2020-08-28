# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 21:59:23
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 22:04:46


class Solution:
	def isSelfCrossing(self, x):

		for i in range(3, len(x)):
			if i >= 3 and x[i-1] <= x[i-3] and x[i] >= x[i-2]:
				return True
			if i >= 4 and x[i-3] == x[i-1] and x[i] + x[i-4] >= x[i-2]:
				return True
			if i >= 5 and x[i] + x[i-4] >= x[i-2] and x[i-1] + x[i-5] >= x[i-3] and x[i-2] > x[i-4] and x[i-3] > x[i-1]:
				return True

		return False