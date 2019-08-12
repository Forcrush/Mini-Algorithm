#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int N=500;  // ���������500��������
int line[N][N];     // line[i][j]��ʾ i �� j �ܻ���ƥ��
int Y[N],used[N];
int m,n;             // X�㼯��m����   Y�㼯��n����

bool found(int x){
    for(int i=1; i<=n; i++){
        if(line[x][i]&&!used[i]){
            used[i]=1;
            if(Y[i]==0 || found(Y[i])){  // ��Y�е� i ���㻹δ��Ի�������Ե�����Ե����ҵ�����·�� (�˵ݹ������)
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
    scanf("%d %d %d",&k,&m,&n); // k���� X����m���� Y����n����
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
