# -*- coding: utf-8 -*-
# @Author: Orange灬Fish
# @Date:   2019-05-04 23:33:33
# @Last Modified by:   Orange灬Fish
# @Last Modified time: 2019-05-05 00:44:04


'''
原字符串s对应的“乱序”串s1，定然满足如下规律：
如果将“乱序”串同样从第i个位置割开，他同样可以形成两个子串，s1[:i]和s1[i:]，并且满足：
s1[:i]是s[:i]的“乱序”且s1[i:]是s[i:]的乱序
或者（因为左右交换的原因）
s1[:i]是s[len(s)-i:]的“乱序”且s1[i:]是s[:len(s)-i]的乱序
'''
class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
        	return False
        # important !!!
        if s1 == s2:
        	return True
        dic = {}
        for i in s1:
        	dic[i] = dic.get(i, 0) + 1
        for j in s2:
        	dic[j] = dic.get(j, 0) - 1
        for item in dic.items():
        	if item[1] != 0:
        		return False
        for i in range(1, len(s1)):
        	if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[len(s1)-i:]) and self.isScramble(s1[i:], s2[:len(s1)-i])):
        		return True
        return False

