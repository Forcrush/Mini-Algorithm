# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-28 22:13:47
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-28 22:36:29


class Solution:
	def countSegments(self, s):
		res = [i for i in s.split() if i]
		return len(res)