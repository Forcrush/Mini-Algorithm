#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int N=500;  // 假设最多有500种配对组合
int line[N][N];     // line[i][j]表示 i 和 j 能互相匹配
int Y[N],used[N];
int m,n;             // X点集有m个点   Y点集有n个点

bool found(int x){
    for(int i=1; i<=n; i++){
        if(line[x][i]&&!used[i]){
            used[i]=1;
            if(Y[i]==0 || found(Y[i])){  // 当Y中第 i 个点还未配对或者已配对但其配对点能找到增广路径 (此递归很巧妙)
                Y[i]=x;
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int x,y;
    int k;
    scanf("%d %d %d",&k,&m,&n); // k条线 X集中m个点 Y集中n个点
    memset(line,0,sizeof(line));
    memset(Y,0,sizeof(Y));
    for(int i=0; i<k; i++){
        scanf("%d %d",&x,&y);
        line[x][y]=1;
    }
    int sum=0;
    for(int i=1; i<=m; i++){
        memset(used,0,sizeof(used));
        if(found(i)) sum++;
    }
    printf("%d\n",sum);
    return 0;
}
