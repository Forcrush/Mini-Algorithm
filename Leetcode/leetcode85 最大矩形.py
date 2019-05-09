# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 12:53:09
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-04 13:25:55


class Solution:
    def maximalRectangle(self, matrix):
        if sum(matrix, []) == []:
        	return 0
        row = len(matrix)
        col = len(matrix[0])
        height = []
        for _ in range(row):
        	height.append([0]*col)
        for i in range(col):
        	height[0][i] = int(matrix[0][i])
        for i in range(1, row):
        	for j in range(col):
        		if matrix[i][j] == '1':
        			height[i][j] = height[i-1][j] + 1
        
        for i in range(row):
        	height[i].append(0)

        maxarea = 0
        for item in height:
        	stack = []
        	for i in range(len(item)):
        		while stack != [] and item[i] < item[stack[-1]]:
        			top = stack.pop()
        			if stack == []:
        				maxarea = max(maxarea, item[top]*i)
        			else:
        				maxarea = max(maxarea, item[top]*(i-stack[-1]-1))
        		stack.append(i)

        return maxarea

