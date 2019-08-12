#include <cstdio>
#include <algorithm>
using namespace std;

int parent[10001];

struct pointpair{
  int a,b,w;
};

bool cmp(const pointpair &x,const pointpair &y){
  return x.w<y.w;
}

void Union(int r1,int r2){
    if(r1==r2) return;
    if(parent[r1]<parent[r2]){
        parent[r1]+=parent[r2];
        parent[r2]=r1;
    }
    else{
        parent[r2]+=parent[r1];
        parent[r1]=r2;
    }
}

int Find(int x){
    if(parent[x]<0) return x;
    else return Find(parent[x]);
}

int main()
{
    int n,m;
    scanf("%d %d",&n,&m);
    pointpair arr[m+1];
    for(int i=1;i<=m;++i) scanf("%d %d %d",&arr[i].a,&arr[i].b,&arr[i].w);
    sort(arr+1,arr+m+1,cmp);
    for(int i=1;i<=n;++i) parent[i]=-1;
    int cnt=0,i=1,vers=0;
    int u,v;
    while(vers!=n-1){
        u=Find(arr[i].a);
        v=Find(arr[i].b);
        if(u!=v){
            Union(u,v);
            vers++;
            cnt+=arr[i].w;
        }
        ++i;
    }
    printf("%d",cnt);
}
