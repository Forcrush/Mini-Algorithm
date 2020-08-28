# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-17 22:18:20
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-18 11:42:10


# 双向 BFS
class Solution:
	def ladderLength(self, beginWord, endWord, wordList):

		if endWord not in wordList or not endWord or not wordList: return 0

		pattern_to_word = {}

		for w in wordList:
			for i in range(len(w)):
				pattern = w[:i] + "*" + w[i+1:]
				if pattern in pattern_to_word:
					pattern_to_word[pattern].append(w)
				else:
					pattern_to_word[pattern] = [w]

		def oneside_bfs(queue, visited, other_visited):

			cur_word, path_len = queue.pop(0)
			for i in range(len(cur_word)):
				intermidiate_pattern = cur_word[:i] + "*" + cur_word[i+1:]
				for w in pattern_to_word.get(intermidiate_pattern, []):
					# 已经被另一个bfs访问
					if w in other_visited:
						return path_len + other_visited[w]
					# 还没被此bfs访问
					if w not in visited:
						visited[w] = path_len + 1
						queue.append((w, path_len+1))

			return None

		begin_side_visited, end_side_visited = {}, {}
		begin_side_visited[beginWord] = 1
		end_side_visited[endWord] = 1

		begin_queue, end_queue = [(beginWord, 1)], [(endWord, 1)]
		while begin_queue and end_queue:
			
			# one execution from begin side
			res = oneside_bfs(begin_queue, begin_side_visited, end_side_visited)
			if res:
				return res

			# one execution from end side
			res = oneside_bfs(end_queue, end_side_visited, begin_side_visited)
			if res:
				return res
				
		return 0

