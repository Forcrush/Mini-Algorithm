# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-24 11:15:26
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-24 11:32:37


'''
桌子上有一堆石头，每次你们轮流拿掉 1 ~ 3 块石头
拿掉最后一块石头的人就是获胜者 你作为先手 你们是聪明人 每一步都是最优解

解 -> 轮到谁时石头还有 4N 个则此人必输

推广1	->	若可拿 1 ~ n 块石头 则轮到谁时石头还有 (n+1)*N 个则此人必输
推广2	->	若可拿 m ~ n 块石头(n > m 且至少有 n 块石头)
			则轮到谁时石头还有 (n+1)*N ~ (n+1)*N+m 个则此人必输
			即当石头数 x: m <= x%(n+1) <= n 时才能赢
'''
class Solution:
	def canWinNim(self, n):
		if n % 4 == 0:
			return False
		return True
