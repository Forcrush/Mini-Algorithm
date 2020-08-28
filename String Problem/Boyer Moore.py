# -*- coding: utf-8 -*-
# @Author: Puffrora
# @Date:   2020-07-01 10:47:25
# @Last Modified by:   Puffrora
# @Last Modified time: 2020-07-01 10:48:54

# reference: https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html


# 预生成坏字符表
def getBMBC(pattern):
    BMBC = {}
    for i in range(len(pattern) - 1):
        # 记录坏字符最右位置（不包括模式串最右侧字符）
        BMBC[pattern[i]] = i + 1
    return BMBC


# 预生成好后缀表
def getBMGS(pattern):
    BMGS = {}

    # 无后缀仅根据坏字移位符规则
    BMGS[''] = 0

    for i in range(len(pattern)):

        # 好后缀
        GS = pattern[len(pattern) - i - 1:]

        for j in range(len(pattern) - i - 1):

            # 匹配部分
            NGS = pattern[j:j + i + 1]

            # 记录模式串中好后缀最靠右位置（除结尾处）
            if GS == NGS:
                BMGS[GS] = len(pattern) - j - i - 1
    return BMGS


# Boyer-Moore算法
def BM(string, pattern):
    m, n = len(pattern), len(string)
    i, j = 0, m
    indies = []
    # 坏字符表
    BMBC = getBMBC(pattern=pattern)
    # 好后缀表
    BMGS = getBMGS(pattern=pattern)  

    while i < n:
        while (j > 0):
            
            # 当无法继续向下搜索就返回值
            if i + j -1 >= n: 
                return indies

            # 主串判断匹配部分
            a = string[i + j - 1:i + m]

            # 模式串判断匹配部分
            b = pattern[j - 1:]

            # 当前位匹配成功则继续匹配
            if a == b:
                j = j - 1

            # 当前位匹配失败根据规则移位
            else:
                i = i + max(BMGS.setdefault(b[1:], m), j - BMBC.setdefault(string[i + j - 1], 0))
                j = m

            # 匹配成功返回匹配位置
            if j == 0:
                indies.append(i)
                i += 1
                j = len(pattern)


a = "bababababcabababadababacambabacaddababacasdsd"
b = "ababab"

# print(BM(a,b))