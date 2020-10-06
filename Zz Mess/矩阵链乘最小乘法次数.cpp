#include <iostream>
using namespace std;

int m[50][50];       //m[i][j]为计算矩阵Ai...j所需的标量乘法运算次数的最小值

void computechain(int *p,int len,int m[50][50],int s[50][50])
{
    int i,j,k,t;
    for(i=0;i<=len;++i) m[i][i] = 0;
    for(t=2;t<=len;t++){                //当前链乘矩阵的长度
        for(i=1;i<=len-t+1;i++){       //从第一矩阵开始算起，计算长度为t的最少代价
            j=i+t-1;                        //长度为t时候的最后一个元素
            m[i][j] = 100000;         //初始化为最大代价
            for(k=i;k<=j-1;k++){        //寻找最优的k值，使得分成两部分k在i与j-1之间
                int temp = m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j];
                if(temp < m[i][j]){
                    m[i][j] = temp;     //记录下当前的最小代价
                    s[i][j] = k;            //记录当前的括号位置，即矩阵的编号
                }
            }
        }
    }
}

int main()
{
    int N;
    cin>>N;  //N个矩阵
    int *p=new int[N+1];
    for(int i=0;i<N+1;i++) cin>>p[i];  //N+1个输入
    for(int i=0;i<50;i++) m[50][50]=0;  //初始化
    computechain(p,N+1,m,s);   //将 i 到 j 的矩阵链乘最小乘法次数最优值存入表
    cout<<m[1][N]<<endl;
    return 0;
}



