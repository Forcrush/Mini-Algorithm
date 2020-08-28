# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-14 21:42:17
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-14 21:54:12


# 寻找循环节
# 时间复杂度 O(|s1|*|s2|) 我们最多找过 |s2|+1 个 s1 就可以找到循环节
# 空间复杂度 O(|s2|) 我们建立的哈希表大小等于 s2 的长度
class Solution:
	def getMaxRepetitions(self, s1, n1, s2, n2):
		if n1 == 0: return 0
		s1_cnt, s2_cnt, index = 0, 0, 0
		visited = {}
		while True:
			s1_cnt += 1
			for c in s1:
				if c == s2[index]:
					index += 1
				if index == len(s2):
					s2_cnt += 1
					index = 0

			# 还没有找到循环节 所有的 s1 就用完了
			if s1_cnt == n1:
				return s2_cnt // n2
			
			# 出现了之前的 index 表示找到了循环节
			if index in visited:
				s1_pre, s2_pre = visited[index]
				# 遇到循环节之前的 s1 个数和 s2 个数
				pre_loop = (s1_pre, s2_pre)
				# 每个循环节里包含的 s1 个数和 s2 个数
				in_loop = (s1_cnt-s1_pre, s2_cnt-s2_pre)
				break
			else:
				visited[index] = (s1_cnt, s2_cnt)

		# ans 存储的是 S1 包含的 s2 的数量 考虑的之前的 pre_loop 和 in_loop
		ans = pre_loop[1] + (n1 - pre_loop[0]) // in_loop[0] * in_loop[1]
		# S1 的末尾还剩下一些 s1 暴力匹配
		rest = (n1 - pre_loop[0]) % in_loop[0]
		for _ in range(rest):
			for c in s1:
				if c == s2[index]:
					index += 1
					if index == len(s2):
						ans += 1
						index = 0

		return ans // n2