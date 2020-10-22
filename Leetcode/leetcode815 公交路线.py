'''
Author: Puffrora
Date: 2020-10-21 18:07:55
LastModifiedBy: Puffrora
LastEditTime: 2020-10-21 23:24:28
'''


class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T: return 0

        from collections import defaultdict, deque

        # 记录每个站的公交种类
        graph = defaultdict(list)
        for bus, route in enumerate(routes):
            for station in route:
                graph[station].append(bus)

        queue = deque([S])
        res = 0
        visited_bus = [0] * len(routes)

        while queue:
            res += 1
            for _ in range(len(queue)):
                cur_station = queue.popleft()
                for bus in graph[cur_station]:
                    if visited_bus[bus]: continue
                    visited_bus[bus] = 1
                    for next_station in routes[bus]:
                        if next_station == T: return res
                        queue.append(next_station)
        
        return -1