'''
Author: Puffrora
Date: 2021-01-27 14:32:27
LastModifiedBy: Puffrora
LastEditTime: 2021-01-27 15:58:25
'''


"""
回溯

策略1
遍历时，如果后面的球与前面的球颜色不一样，在这里尝试插入一个后面颜色的球
输入: "RRWWRRBBRR", "WB"
输出: 2
解释: RRWWRRBBRR -> R[B]RWWRRBBRR -> R[B]RWW[W]RRBBRR -> ... -> empty

策略2
如果相邻的两个球颜色相同，考虑在中间插入一个其他颜色的球，将他们分割
输入: "RRYGGYYRRYGGYYRR", "GGBBB"
输出: 5
解释: RRYGGYYR[B]RYGGYYRR -> RRYG[G]GYYR[B]RYG[G]GYYRR -> ... -> [B][B][B]

链接：https://leetcode-cn.com/problems/zuma-game/solution/488-by-ikaruga/
"""
class Solution:
    def findMinStep(self, board, hand):

        from collections import Counter

        have = Counter(hand)
        cnt = len(hand)
        res = float('inf')

        def eliminate(ballline):
            for i in range(len(ballline)-2):
                j = i + 1
                while j < len(ballline) and ballline[i] == ballline[j]:
                    j += 1
                if j - i < 3:
                    i = j - 1
                    continue
                ballline = ballline[:i] + ballline[j:]
                return eliminate(ballline)
            return ballline

        def dfs(ballline, step):
            nonlocal res, cnt

            ballline = eliminate(ballline)
            if ballline == '':
                res = min(res, step)
            
            if step == cnt: return
            if step >= res: return
            
            pos_insert = set()
            for i in range(len(ballline)):
                if i == 0 or ballline[i] != ballline[i-1]:
                    if have[ballline[i]] != 0:
                        pos_insert.add((i, ballline[i]))
                if i != 0 and ballline[i] == ballline[i-1]:
                    for k, v in have.items():
                        if k == ballline[i] or v == 0:
                            continue
                        pos_insert.add((i, k))

            for pos, ball in pos_insert:
                have[ball] -= 1
                ballline = ballline[:pos] + ball + ballline[pos:]
                dfs(ballline, step+1)
                ballline = ballline[:pos] + ballline[pos+1:]
                have[ball] += 1

        dfs(board, 0)
        return res if res != float('inf') else -1


print(Solution().findMinStep("RRWWRRBBRR", "WB"))
print(Solution().findMinStep("RRYGGYYRRYGGYYRR", "GGBBB"))
print(Solution().findMinStep("RRYGGYYRRYGGYYRR", "GGBBB"))
