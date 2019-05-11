# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-10 13:53:17
# @Last Modified by:   Hongyu Chen
# @Last Modified time: 2019-05-10 17:06:00


class Solution:
	def integerReplacement(self, n):
		if n == 1:
			return 0
		if n % 2 == 0:
			return self.integerReplacement(n / 2) + 1
		else:
			return min(self.integerReplacement(n - 1), self.integerReplacement(n + 1)) + 1

