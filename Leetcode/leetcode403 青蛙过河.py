# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-09-19 12:23:34
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-09-19 13:45:17


class Solution:
	def canCross(self, stones):
		stone_dic = {}
		for i in stones:
			stone_dic[i] = set()
		stone_dic[0].add(0)
		for i in range(len(stones)):
			for step in stone_dic[stones[i]]:
				for maybe_step in range(max(1, step-1), step+2):
					next_pos = stones[i] + maybe_step
					if next_pos in stone_dic:
						stone_dic[next_pos].add(maybe_step)

		return True if stone_dic[stones[-1]] else False
