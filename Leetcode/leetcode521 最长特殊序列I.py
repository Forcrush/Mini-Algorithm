# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-02-17 13:42:26
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-02-17 13:44:01


class Solution:
	def findLUSlength(self, a, b):
		return -1 if a == b else max(len(a), len(b))