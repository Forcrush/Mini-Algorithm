class Solution:
    def searchMatrix(self, matrix, target):
        if sum(matrix, []) == []:
        	return False
        row = len(matrix)
        col = len(matrix[0])

        # Find row
        if matrix[row//2][0] > target:
        	rowend = row // 2
        	rowstart = 0
        elif matrix[row//2][0] < target:
        	rowstart = row // 2
        	rowend = row - 1
        else:
        	return True
        while rowend - rowstart > 1:
        	rowmid = (rowstart + rowend) // 2
        	if matrix[rowmid][0] > target:
        		rowend = rowmid
        	elif matrix[rowmid][0] < target:
        		rowstart = rowmid
        	else:
        		return True
        # rowend - rowstart == 1
        if matrix[rowend][0] == target:
        	return True
        elif matrix[rowend][0] < target:
        	rowstart = rowend
        # Find col
        colstart = 0
        colend = col - 1
        while colstart <= colend:
        	colmid = (colstart + colend) // 2
        	if matrix[rowstart][colmid] < target:
        		colstart = colmid + 1
        	elif matrix[rowstart][colmid] > target:
        		colend = colmid - 1
        	else:
        		return True

        return False