# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2019-09-27 17:57:36
# @Last Modified by:   Puffrora
# @Last Modified time: 2019-09-27 18:30:37


class Solution:
	def canConstruct(self, ransomNote, magazine):
		ran_dic, mag_dic ={}, {}
		for i in ransomNote:
			ran_dic[i] = ran_dic.get(i, 0) + 1
		for  j in magazine:
			mag_dic[j] = mag_dic.get(j, 0) + 1
		for key,val in ran_dic.items():
			if key not in mag_dic:
				return False
			elif mag_dic[key] < val:
				return False
		return True

