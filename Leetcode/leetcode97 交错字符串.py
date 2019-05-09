# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-05 17:24:11
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-05 18:01:20


'''
dp[i][j]表示s1的前i个字符和s2的前j个字符能否交错成s3的前i+j个字符
状态转移方程:
			dp[i-1][j](if true)	if s3[i+j-1] == s1[i-1]
		   /
dp[i][j] =
		   \
			dp[i][j-1](if true)	if s3[i+j-1] == s2[j-1]
'''
class Solution:
    def isInterleave(self, s1, s2, s3):
    	if s1 == '':
    		return s2 == s3
    	if s2 == '':
    		return s1 == s3
    	if s3 == '':
    		return s1 == '' and s2 == ''
    	len1 = len(s1)
    	len2 = len(s2)
    	if len1 + len2 != len(s3):
    		return False
    	dp = []
    	for i in range(len1+1):
    		dp.append([False]*(len2+1))

    	for i in range(len1):
    		if s1[i] == s3[i]:
    			dp[i+1][0] = True
    		else:
    			break
    	for j in range(len2):
    		if s2[j] == s3[j]:
    			dp[0][j+1] = True
    		else:
    			break

    	for i in range(1, len1+1):
    		for j in range(1, len2+1):
    			if s3[i+j-1] == s1[i-1]:
    				if dp[i-1][j]:
    					dp[i][j] = dp[i-1][j]
    			if s3[i+j-1] == s2[j-1]:
    				if dp[i][j-1]:
    					dp[i][j] = dp[i][j-1]
    	'''
    	for i in range(len1+1):
    		print(dp[i])
		'''
    	return dp[len1][len2]
'''
s1 = "aabc"
s2 = "abad"
s3 = "aabadabc"
'''