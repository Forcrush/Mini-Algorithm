'''
Author: Puffrora
Date: 2021-01-26 11:52:07
LastModifiedBy: Puffrora
LastEditTime: 2021-01-26 13:36:24
'''


class Trie:
    def __init__(self):
        from collections import OrderedDict

        # 使用orderdict保持字典序前缀树
        self.root = OrderedDict()
        self.cnt = 3
        self.buffer = []
    
    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        # ‘#’标志来储存整个单词
        root['#'] = word
    
    def dfs(self, node):
        if self.cnt <= 0: return
        
        if '#' in node:
            self.buffer.append(node['#'])
            self.cnt -= 1
        
        for child in node:
            if child == '#':
                continue
            self.dfs(node[child])
        
    def find_prefix(self, s_word):
        res = []
        root = self.root
        for c in s_word:
            if c not in root:
                res.append([])
                root = {}
            else:
                self.dfs(root[c])
                res.append(self.buffer)

                # 更新重置
                self.cnt = 3
                self.buffer = []
                root = root[c]
                
        return res


class Solution:
    def suggestedProducts(self, products, searchWord):

        trie = Trie()

        for word in sorted(products):
            trie.insert(word)
            
        return trie.find_prefix(searchWord)

