'''
Author: Puffrora
Date: 2020-10-11 19:50:51
LastModifiedBy: Puffrora
LastEditTime: 2020-10-11 20:24:21
'''


"""
特殊情况
1. 小于等于10的数，返回n-1
2. 10的幂，返回n-1
3. 若干个9，返回n+2
4. 11，这个数字比较特殊，返回9

普通情况
首先把n从中间分成a、b两部分，如果长度是奇数就给a多分点
然后用a、a+1、a-1为左边分别构建一个回文数，注意n长度为奇数的时候a最右边的一个字符即原字符串中间那个字符不能复制过去
最后选取离n最近且不为n的结果即可
"""
class Solution:
    def nearestPalindromic(self, n):
        if int(n) < 10 or int(n[::-1]) == 1:
            return str(int(n)-1)
        if set(n) == {'9'}:
            return str(int(n)+2)
        if n == '11':
            return '9'
        
        a, b = n[:(len(n)+1)//2], n[(len(n)+1)//2:]
        tmp = [str(int(a)-1), a, str(int(a)+1)]
        tmp = [i + i[len(b)-1::-1] for i in tmp]
        tmp.sort(key=lambda x: abs(int(x)-int(n)))
        
        return tmp[1] if tmp[0] == n else tmp[0]


