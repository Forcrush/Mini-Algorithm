# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-01 11:29:13
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-01 11:33:55


class Solution:
	def lexicalOrder(self, n):

		res = []

		def dfs(root):
			if root > n:
				return
			res.append(root)
			for i in range(10):
				dfs(10*root+i)

		for i in range(1, 10):
			dfs(i)

		return res