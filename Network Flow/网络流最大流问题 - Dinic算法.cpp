/*
 * @Author: Puffrora
 * @Date: 2020-10-27 21:22:21
 * @LastModifiedBy: Puffrora
 * @LastEditTime: 2020-10-27 21:46:21
 */

// https://blog.nowcoder.net/n/6ef60bf52036463eb892c89bbdc178ed

#include <iostream>
#include <string.h>
#include <queue>
using namespace std;
int const inf = 0x3f3f3f3f;
int const MAX = 205;
int n, m, start, target;
int c[MAX][MAX], dep[MAX]; //dep[MAX]代表当前层数

int bfs(int s, int t) //重新建图，按层次建图
{
    queue<int> q;
    while (!q.empty())
        q.pop();
    memset(dep, -1, sizeof(dep));
    dep[s] = 0;
    q.push(s);
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int v = 1; v <= m; v++)
        {
            if (c[u][v] > 0 && dep[v] == -1)
            { //如果可以到达且还没有访问，可以到达的条件是剩余容量大于0，没有访问的条件是当前层数还未知
                dep[v] = dep[u] + 1;
                q.push(v);
            }
        }
    }
    return dep[t] != -1;
}

int dfs(int u, int mi, int t) //查找路径上的最小流量
{
    if (u == t)
        return mi;
    int tmp;
    for (int v = 1; v <= m; v++)
    {
        if (c[u][v] > 0 && dep[v] == dep[u] + 1 && (tmp = dfs(v, min(mi, c[u][v]), t)))
        {
            c[u][v] -= tmp;
            c[v][u] += tmp;
            return tmp;
        }
    }
    return 0;
}

int dinic(int s, int t)
{
    int ans = 0, tmp;
    while (bfs(s, t))
    {
        while (1)
        {
            tmp = dfs(s, inf, t);
            if (tmp == 0)
                break;
            ans += tmp;
        }
    }
    return ans;
}

int main()
{
    // n 是边数 m 是节点数 start 是源点 target 是汇点
    while (~scanf("%d %d %d %d", &n, &m, &start, &target))
    {
        memset(c, 0, sizeof(c));
        int u, v, w;
        while (n--)
        {
            scanf("%d %d %d", &u, &v, &w);
            c[u][v] += w;
        }
        //
        printf("%d\n", dinic(start, target));
    }
    return 0;
}