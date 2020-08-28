# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-08-02 21:29:20
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-08-02 22:21:04


# 判断有向图是否存在环


# 拓扑排序 找入度为0的结点 如果没有且图不为空则必存在环
class Solution:
	def canFinish(self, numCourses, prerequisites):

		dic = {}
		'''
		dic: {node : [indegree, child1, child2, child3, ...], ...}
		'''
		for item in prerequisites:
			# add child nodes
			dic[item[1]] = dic.get(item[1], [0])
			dic[item[1]].append(item[0])
			# add indegree
			dic[item[0]] = dic.get(item[0], [0])
			dic[item[0]][0] += 1

		while True:
			flag = False
			for k,v in dic.items():
				if v[0] == 0:
					vertex = dic.pop(k)
					for child in vertex[1:]:
						dic[child] = dic.get(child, [0])
						dic[child][0] -= 1
					flag = True
					break

			if len(dic) == 0:
				return True
			if not flag and len(dic) > 0:
				return False


# DFS
class Solution:
	def canFinish(self, numCourses, prerequisites):

		'''
		flag
		未被 DFS 访问：i == 0；
		已被其他节点启动的 DFS 访问：i == -1；
		已被当前节点启动的 DFS 访问：i == 1
		'''
		def dfs(i, adjacency, flag):
			if flag[i] == -1: return True
			if flag[i] == 1: return False
			flag[i] = 1
			for j in adjacency[i]:
				if not dfs(j, adjacency, flag):
					return False
			flag[i] = -1
			return True

		adjacency = [[] for _ in range(numCourses)]
		flag = [0 for _ in range(numCourses)]

		for item in prerequisites:
			adjacency[item[1]].append(item[0])
		for i in range(numCourses):
			if not dfs(i, adjacency, flag):
				return False
		return True