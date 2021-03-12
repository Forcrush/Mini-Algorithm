'''
Author: Puffrora
Date: 2021-03-12 09:50:10
LastModifiedBy: Puffrora
LastEditTime: 2021-03-12 10:35:28
'''


from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        from collections import defaultdict

        node = {}
        for i, l in enumerate(languages):
            if i+1 not in node:
                node[i+1] = defaultdict(dict)
            node[i+1]['L'] = set(l)
        for a, b in friendships:
            small, big = min(a, b), max(a, b)
            if 'F' not in node[small]:
                node[small]['F'] = set([big])
            else:
                node[small]['F'].add(big)

        # 找出不可以互相交流的人 并记录他们已经会的语言
        lang = [0] * (n + 1)
        person = set()
        for k in node.keys():
            for f in node[k]['F']:
                if not node[k]['L'].intersection(node[f]['L']):
                    if k not in person:
                        person.add(k)
                        for l in node[k]['L']:
                            lang[l] += 1
                    if f not in person:
                        person.add(f)
                        for l in node[f]['L']:
                            lang[l] += 1
        
        return len(person) - max(lang)

