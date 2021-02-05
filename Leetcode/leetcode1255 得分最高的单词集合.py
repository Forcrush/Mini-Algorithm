'''
Author: Puffrora
Date: 2021-02-05 16:53:25
LastModifiedBy: Puffrora
LastEditTime: 2021-02-05 18:20:39
'''


class Solution:
    def maxScoreWords(self, words, letters, score):

        from collections import Counter

        def getPoints(word):
            points = 0
            for c in word:
                points += score[ord(c)-ord('a')]
            return points

        def search(cur_have, left, right):
            if left >= right:
                return 0

            tmp = search(cur_have, left+1, right)
            cur_word = Counter(words[left])
            check = all(cur_have[k] >= v for k, v in cur_word.items())
            if check:
                cur_have -= cur_word
                tmp = max(tmp, getPoints(
                    words[left]) + search(cur_have, left+1, right))
                cur_have += cur_word
            return tmp

        cur_have = Counter(letters)

        return search(cur_have, 0, len(words))


# ! why variable 'have' changed ???
class Solution_issue:
    def maxScoreWords(self, words, letters, score):

        from collections import defaultdict

        have = defaultdict(int)
        for l in letters:
            have[l] += 1
        print('---', have)

        def getPoints(word):
            points = 0
            for c in word:
                points += score[ord(c)-ord('a')]
            return points

        curUsed = [0] * 26
        
        def search(curUsed, left, right):
            
            if left >= right:
                return 0

            tmp =  search(curUsed, left+1, right)
            print(left, have)
            flag = True
            for w in words[left]:
                curUsed[w] += 1
            for k, v in curUsed.items():
                if v > have[k]:
                    flag = False
            
            if flag:
                for c in words[left]:
                    curUsed[ord(c)-ord('a')] += 1
                tmp = max(tmp, getPoints(words[left]) + search(curUsed, left+1, right))
                
            return tmp

        curUsed = defaultdict(int)
        return search(curUsed, 0, len(words))


w = ["dog", "cat", "dad", "good"]
l = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
s = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(Solution().maxScoreWords(w, l, s))
print(Solution_issue().maxScoreWords(w, l, s))
