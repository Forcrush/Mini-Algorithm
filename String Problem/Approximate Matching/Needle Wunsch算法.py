# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-08-17 12:23:56
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-08-29 09:31:20



'''
			史密斯-沃特曼算法					尼德曼-翁施算法
初始化阶段	第一行和第一列全填充为 0			首行和首列需要考虑空位罚分
打分阶段		若得分为负，则分数为零			得分可以为负
回溯阶段		从最高分开始，回溯直至得分为 0		从右下角开始，回溯至左上角

尼德曼-翁施算法是全局比对算法(Needleman-Wunsch Algorithm)也被称为优化匹配算法和整体序列比较法
'''
def Needle_Wunsch(s1, s2):
	l1, l2 = len(s1), len(s2)
	matrix = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

	# Action Cost
	match = 1
	delete, insert, replace = -1, -1, -1
	"""
	当 match = 0
	delete, insert, replace = 1, 1, 1 时
	最终结果就是 Levenshitein 距离
	"""
	for i in range(1, len(s1)+1):
		matrix[i][0] = i * insert
	for j in range(1, len(s2)+1):
		matrix[0][j] = j * delete

	for i in range(1, len(s1)+1):
		for j in range(1, len(s2)+1):
			# match
			if s1[i-1] == s2[j-1]:
				matrix[i][j] = matrix[i-1][j-1] + match
			else:
				# max(insert, delete, replace)
				# min(insert, delete, replace) if match < insert, delete, replace
				matrix[i][j] = max(matrix[i-1][j]+insert, matrix[i][j-1]+delete, matrix[i-1][j-1]+replace)
	
	return matrix[len(s1)][len(s2)]

