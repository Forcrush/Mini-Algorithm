'''
Author: Puffrora
Date: 2021-01-16 21:39:55
LastModifiedBy: Puffrora
LastEditTime: 2021-01-16 22:33:35
'''


"""
贪心算法
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560/JavaC%2B%2BPython-Easy-Greedy-with-Prove
"""
class Solution:
    def longestDecomposition(self, text):
        
        def greedy_recursion(s, res):
            n = len(s)
            for l in range(1, n//2+1):
                if s[0] == s[n-l] and s[l-1] == s[-1]:
                    if s[:l] == s[n-l:]:
                        return greedy_recursion(s[l:n-l], res+2)
            
            return res + 1 if s else res
        
        return greedy_recursion(text, 0)
    
