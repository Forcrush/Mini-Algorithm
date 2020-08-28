# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-05 11:28:45
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-05 13:38:02


class Solution:
	def wordBreak(self, s, wordDict):

		memo = {}

		def traceback(start, end):
			res = []
			if start > end:
				return [[]]

			else:
				for i in range(start, end+1):
					if s[start:i+1] in wordDict:
						if i+1 in memo:
							new_part = memo[i+1]
						else:
							new_part = traceback(i+1, end)
						for p in new_part:
							tmp = [s[start:i+1]] + p
							res.append(tmp)

			memo[start] = res
			return res

		final_res = traceback(0, len(s)-1)
		if not final_res: return []
		
		new_final_res = []
		for item in final_res:
			new_final_res.append(" ".join(item))
		return new_final_res

