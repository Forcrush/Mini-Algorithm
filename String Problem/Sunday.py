# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-01-07 13:58:15
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-01-07 14:18:47


# 记录每个字符在字符串中出现的位置 若有重复字符则记录其最晚出现的位置
def char_pos(s):
	dic = {}
	for i in range(len(s)):
		dic[s[i]] = i
	return dic


def Sunday(p, s):
	plen, slen = len(p), len(s)
	dic = char_pos(s)
	# 主串和子串的位置指针
	pp, sp = 0, 0
	pointer = 0
	res = []
	while pointer <= plen - slen:
		pp = pointer
		sp = 0

		while pp < plen and sp < slen and p[pp] == s[sp]:
			pp += 1
			sp += 1
		if sp == slen:
			res.append(pointer)
			
		# 匹配失败时关注的是主串中参加匹配的最末位字符的下一位字符
		# 如果该字符没有在模式串中出现则直接跳过 即移动位数 = 模式串长度 + 1
		# 否则移动位数 = 模式串长度 - 该字符最右出现的位置(以0开始) = 模式串中该字符最右出现的位置到尾部的距离 + 1
		if pointer + slen < plen:
			pointer += slen - dic.get(p[pointer+slen], -1)
		else:
			break
	return res


a = "babababacbababadababacambabacaddababacasdsd"
b = "ababa"

print(Sunday(a,b))