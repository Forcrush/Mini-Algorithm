# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-12-16 16:10:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-12-16 16:13:21


class Solution:
	def rangeBitwiseAnd(self, m, n):
		cnt = 0
		while m != n:
			m >>= 1
			n >>= 1
			cnt += 1
		return m << cnt

		