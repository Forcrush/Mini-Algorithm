'''
Author: Puffrora
Date: 2021-03-04 14:08:40
LastModifiedBy: Puffrora
LastEditTime: 2021-03-04 14:48:26
'''


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        if not root: return []

        to_delete = set(to_delete)
        res = [] if root.val in to_delete else [root]

        def dfs(node, parent, flag):
            if not node: return

            dfs(node.left, node, 'L')
            dfs(node.right, node, 'R')

            if node.val in to_delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                if flag == 'L':
                    parent.left = None
                if flag == 'R':
                    parent.right = None
        
        dfs(root, None, None)

        return res
