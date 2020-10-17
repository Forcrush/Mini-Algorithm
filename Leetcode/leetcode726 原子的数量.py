'''
Author: Puffrora
Date: 2020-10-14 21:00:56
LastModifiedBy: Puffrora
LastEditTime: 2020-10-14 21:12:33
'''


class Solution:
    def countOfAtoms(self, formula):

        from collections import Counter

        stack = [Counter()]
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                tmp = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multipier = int(formula[tmp:i] or 1)
                top = stack.pop()
                for k, v in top.items():
                    stack[-1][k] += multipier * v
            else:
                tmp = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                name = formula[tmp: i]
                tmp = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                multipier = int(formula[tmp:i] or 1)
                stack[-1][name] += multipier
        
        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else "") for name in sorted(stack[-1]))

