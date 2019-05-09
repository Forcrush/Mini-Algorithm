# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 01:11:10
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-04 01:51:42


# Solution 1 :
# Space Cost -- O(m + n) with less time cost
class Solution1:
    def setZeroes(self, matrix):
    	row = len(matrix)
    	col = len(matrix[0])
    	markrow = [1] * row
    	markcol = [1] * col
    	for i in range(row):
    		for j in range(col):
    			if matrix[i][j] == 0:
    				markrow[i] = 0
    				markcol[j] = 0

    	for i in range(row):
    		for j in range(col):
    			if markrow[i] == 0 or markcol[j] == 0:
    				matrix[i][j] = 0
    	
    	# return matrix


# Solution 2 (原地算法) :
# Space Cost -- O(1) with more time cost
class Solution2:
    def setZeroes(self, matrix):
    	# 1st step : find a row without 0, if it doesn't exist all postion will be set as 0
    	row = len(matrix)
    	col = len(matrix[0])
    	nonzerorow = -1
    	for i in range(row):
    		index = 0
    		for j in range(col):
    			if matrix[i][j] == 0:
    				break
    			else:
    				index += 1
    		if index == col:
    			nonzerorow = i
    			break
    	if nonzerorow == -1:
    		for i in range(row):
    			for j in range(col):
    				matrix[i][j] = 0
    	else:
    		# 2nd step
    		for i in range(row):
    			if i == nonzerorow:
    				continue
    			for j in range(col):
    				if matrix[i][j] == 0:
    					matrix[nonzerorow][j] = 0
    		# 3rd step
    		for i in range(row):
    			if i == nonzerorow:
    				continue
    			for j in range(col):
    				if matrix[i][j] == 0:
    					for k in range(col):
    						matrix[i][k] = 0
    					break
    		# 4th step
    		for j in range(col):
    			if matrix[nonzerorow][j] == 0:
    				for i in range(row):
    					matrix[i][j] = 0

    	# return matrix

