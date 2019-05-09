# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 00:44:45
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-04 01:10:02

class Solution:
    def spiralOrder(self, matrix):
        if matrix == []:
        	return []
        row = len(matrix)
        col = len(matrix[0])
        if row == 1 or col == 1:
        	return sum(matrix, [])
        rowbegin = 0
        rowend = row - 1
        colbegin = 0
        colend = col - 1
        res = []
        num = 1
        while num <= row * col:

        	for i in range(colbegin, colend + 1):
        		res.append(matrix[rowbegin][i])
        		num += 1
        	rowbegin += 1
        	if rowbegin > rowend:
        		break

        	for i in range(rowbegin, rowend + 1):
        		res.append(matrix[i][colend])
        		num += 1
        	colend -= 1
        	if colend < colbegin:
        		break

        	for i in range(colend, colbegin - 1, -1):
        		res.append(matrix[rowend][i])
        		num += 1
        	rowend -= 1
        	if rowend < rowbegin:
        		break

        	for i in range(rowend, rowbegin - 1, -1):
        		res.append(matrix[i][colbegin])
        		num += 1
        	colbegin += 1
        	if colbegin > colend:
        		break

        return res
        
