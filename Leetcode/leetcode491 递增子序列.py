# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-18 13:42:31
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-18 14:34:45


class Solution:
	def findSubsequences(self, nums):

		res = []

		def dfs(arr, tmp):
			if len(tmp) > 1:
				res.append(tmp)

			cur_ele = set()
			for idx, n in enumerate(arr):
				if n in cur_ele:
					continue
				if not tmp or n >= tmp[-1]:
					cur_ele.add(n)
					dfs(arr[idx+1:], tmp+[n])

		dfs(nums, [])
		
		return res
