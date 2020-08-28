# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-02-14 11:44:43
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-02-14 11:56:33


# 可以看成寻找 B 是否为 某个 kA 的子串
# 其中 kA 的长度在 [B, B+2*A] 之间
class Solution:
	def repeatedStringMatch(self, A, B):
		k = 1
		while k * len(A) < len(B):
			k += 1
		begin = k
		while k * len(A) < len(B) + 2 * len(A):
			k += 1
		end = k
		# k 的范围
		for i in range(begin, end+1):
			# 这里判断子串存在用了内置函数 也可以自己用 KMP / Rabin-Karp 等算法实现
			if B in i*A:
				return i
		return -1

		