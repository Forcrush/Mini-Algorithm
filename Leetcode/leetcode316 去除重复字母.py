# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-19 16:09:46
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-19 16:22:25


class Solution:
	def removeDuplicateLetters(self, s):
		if not s: return s

		last_pos = {c:pos for pos, c in enumerate(s)}
		
		stack = [s[0]]
		seen = set()
		seen.add(s[0])
		for i in range(1, len(s)):
			if s[i] not in seen:
				while stack and s[i] < stack[-1] and last_pos[stack[-1]] > i:
					seen.discard(stack.pop())
				seen.add(s[i])
				stack.append(s[i])

		return "".join(stack)

