#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int map[300][300];
int used[300];
int n,m;
const int INF = 1000000000;

int dfs(int s,int t,int f)
{
    if(s == t) return f;
    for(int i = 1 ; i <= n ; i ++) {
        if(map[s][i] > 0 && !used[i]) {
            used[i] = true;
            int d = dfs(i,t,min(f,map[s][i]));
            if(d > 0) {
                map[s][i] -= d;
                map[i][s] += d;
                return d;
            }
        }
    }
}

int maxflow(int s,int t)
{
    int flow = 0;
    while(true) {
        memset(used,0,sizeof(used));
        int f = dfs(s,t,INF);//不断找从s到t的增广路
        if(f == 0) return flow;//找不到了就回去
        flow += f;//找到一个流量f的路
    }
}

int main()
{
    while(scanf("%d%d",&m,&n) != EOF) {  //m条边，n个点且n为汇点
        memset(map,0,sizeof(map));
        for(int i = 0 ; i < m ; i ++) {
            int from,to,cap;
            scanf("%d%d%d",&from,&to,&cap);
            map[from][to] += cap;
        }
        cout << maxflow(1,n) << endl;
    }
    return 0;
}
