'''
Author: Puffrora
Date: 2020-12-08 17:47:48
LastModifiedBy: Puffrora
LastEditTime: 2020-12-08 17:58:02
'''


'''
可以转换为 寻找一个数组中相邻元素差为 1 连续子数组的总个数
注意此题中 z 与 a 是特例
'''
class Solution:
    def findSubstringInWraproundString(self, p):

        from collections import defaultdict

        # ! 细节处理
        p = '#' + p
        
        # ! 记录以当前字母结尾的且符合题意的连续数组个数
        window = 1

        # ! key 是字母， value 是长度  记录以 key 结尾的最长连续子串的长度
        len_mapper = defaultdict(int)
        
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i-1]) in [1, -25]:
                window += 1
            else:
                window = 1
            
            # ! 只用记录以 key 结尾的长连续子串的最长长度 避免重复 如 'cac'
            len_mapper[p[i]] = max(len_mapper[p[i]], window)

        return sum(len_mapper.values())


