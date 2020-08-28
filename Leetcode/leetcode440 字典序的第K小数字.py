# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-13 19:19:12
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-14 15:00:30


class Solution:
	def findKthNumber(self, n, k):

		# 计算当前前缀 prefix 下小于 n 的节点数目
		def get_cnt(prefix, n):
			cur, nex = prefix, prefix+1
			cnt = 0
			# 当前的前缀当然不能大于上界 n
			while cur <= n:
				cnt += min(nex, n+1) - cur
				cur *= 10
				nex *= 10
				'''
				如果说刚刚prefix是1，next是2，那么现在分别变成10和20
				1为前缀的子节点增加10个，十叉树增加一层, 变成了两层

				如果说现在prefix是10，next是20，那么现在分别变成100和200，
				1为前缀的子节点增加100个，十叉树又增加了一层，变成了三层
				'''
			return cnt
		
		# pos 为排位第 pos 的节点
		pos, prefix = 1, 1
		while pos < k:
			count = get_cnt(prefix, n)
			# 第 k 个数在当前前缀下
			if pos + count > k:
				prefix *= 10
				pos += 1

			# 第 k 个数不在当前前缀下
			else:
				prefix += 1
				pos += count

		return prefix

