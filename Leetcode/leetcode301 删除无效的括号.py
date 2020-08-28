# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-09 00:34:15
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-10 19:42:51


class Solution:
	def removeInvalidParentheses(self, s):

		# record left-bra right-bra that should be deleted
		left, right = 0, 0
		for i in s:
			if i == '(':
				left += 1
			elif i == ")":
				if left == 0:
					right += 1
				else:
					left -= 1

		res = set()

		def backtracking(start, left_cnt, right_cnt, left_rem, right_rem, path):
			
			if start == len(s):
				if left_rem == 0 and right_rem == 0:
					res.add("".join(path))
			else:
				if (s[start] == "(" and left_rem > 0) or (s[start] == ")" and right_rem > 0):
					backtracking(start+1, left_cnt, right_cnt, left_rem-(s[start] == "("), right_rem-(s[start] == ")"), path)

				# use same array instead of path[:] + [s[start]], to save memory
				path.append(s[start])

				if s[start] != "(" and s[start] != ")":
					backtracking(start+1, left_cnt, right_cnt, left_rem, right_rem, path)
				elif s[start] == "(":
					backtracking(start+1, left_cnt+1, right_cnt, left_rem, right_rem, path)
				elif s[start] == ")" and left_cnt> right_cnt:
					backtracking(start+1, left_cnt, right_cnt+1, left_rem, right_rem, path)

				# pop for backtracking
				path.pop()
		backtracking(0,0,0,left,right,[])
		return list(res)
