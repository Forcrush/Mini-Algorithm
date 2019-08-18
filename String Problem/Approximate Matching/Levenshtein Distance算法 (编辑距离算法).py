# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-17 12:23:13
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-17 12:58:24


def LD(s1, s2):
	l1, l2 = len(s1), len(s2)
	matrix = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

	# Action Cost
	match = 0
	delete, insert, replace = 1, 1, 1

	for i in range(1, len(s1)+1):
		matrix[i][0] = i
	for j in range(1, len(s2)+1):
		matrix[0][j] = j

	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			# match
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + match
			else:
				matrix[i][j] = min(matrix[i-1][j]+insert, matrix[i][j-1]+delete, matrix[i-1][j-1]+replace)
	
	return matrix[len(s1)][len(s2)]

