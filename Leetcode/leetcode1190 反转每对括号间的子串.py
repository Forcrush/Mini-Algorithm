'''
Author: Puffrora
Date: 2021-01-21 16:41:15
LastModifiedBy: Puffrora
LastEditTime: 2021-01-21 18:32:28
'''


class Solution:
    def reverseParentheses(self, s):
        
        res = ['']
        for c in s:
            if c == '(':
                res.append('')
            elif c == ')':
                res[-2] += res[-1][::-1]
                res.pop()
            else:
                res[-1] += c
        
        return res[0]


# . Amazing Idea !!!
class Solution1:
    def reverseParentheses(self, s):

        stack = []
        pair = [0] * len(s)
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
            
        i, d = -1, 1
        res = ''
        while (i := i+d) < len(s):
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                res += s[i]

        return res
