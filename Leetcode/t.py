'''
Author: Puffrora
Date: 2019-05-04 23:31:54
LastModifiedBy: Puffrora
LastEditTime: 2021-01-27 13:49:21
'''
# 3=/76=/239=/424=/438=/480=/567=/992=/1176/715=/850=/968
# 466=/1248/629=/493=/218=/214=/854=/1420
# 842/828
# https://careers.google.com/jobs/results/88312509183730374-technical-solutions-engineer-big-data-and-machine-learning/?company=Google&company=YouTube&hl=zh_CN&hl=zh_CN&jlo=en-US&location=Sydney%20NSW,%20Australia&page=3

# To review: 699 * 730 * 753 * 801 * 850 * 1187
''',
Mendeley
Zotero
https://www.jvruo.com/archives/455/
'''


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        import collections
        def backtrack(board):
            if not board:
                return 0
            i = 0
            ans = 6
            while i < len(board):
                j = i + 1
                while j < len(board) and board[i] == board[j]:
                    j += 1
                balls = 3 - (j - i)
                if counter[board[i]] >= balls:
                    balls = max(0, balls)
                    counter[board[i]] -= balls
                    ans = min(ans, balls + backtrack(board[:i] + board[j:]))
                    counter[board[i]] += balls
                i = j
            return ans

        counter = collections.Counter(hand)
        ans = backtrack(board)
        return -1 if ans > 5 else ans


print(Solution().findMinStep("WWBBWBBWW", "BB"))


def cal_next(s, length):

    next = [-1] * length  
    k = -1 
    for q in range(1, length):
        while k > -1 and s[k+1] != s[q]: 
            k = next[k]  
        if s[k + 1] == s[q]: 
            k = k + 1;
        next[q] = k; 
    return next  
    
def KMP(s, p):
    slen = len(s)
    plen = len(p)
    pos = []
    next = cal_next(p, plen)  
    k = -1
    i = 0
    while i < slen:
        while k > -1 and p[k + 1] != s[i]:  
            k = next[k]  
        if p[k + 1] == s[i]:
            k = k + 1;
        if k == plen-1:
            pos.append(i-plen+1)
            k = -1  
            i = i - plen + 1  
        i += 1
    return pos


a = "bababababcabababadababacambabacaddababacasdsd"
b = "ababab"


# print(KMP(a,b))
