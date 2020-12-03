'''
Author: Puffrora
Date: 2020-11-16 12:09:33
LastModifiedBy: Puffrora
LastEditTime: 2020-11-16 16:06:32
'''


class Trie:
    def __init__(self):
        self.root = {}
        # 记录所有子树高度之和
        self.all_height = 0

    def insert(self, word):
        root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
    
    def bfs(self, root, depth):
        if len(root) == 0:
            # ! +1 because of the '#' symbol
            self.all_height += depth + 1
            return
        for c in root:
            self.bfs(root[c], depth+1)

    def get_all_height(self):
        self.bfs(self.root, 0)
        return self.all_height


class Solution:
    def minimumLengthEncoding(self, words):
        
        trie = Trie()

        for w in words:
            trie.insert(w[::-1])
        
        return trie.get_all_height()

