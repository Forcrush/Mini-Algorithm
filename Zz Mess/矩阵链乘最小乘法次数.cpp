#include <iostream>
using namespace std;

int m[50][50];       //m[i][j]Ϊ�������Ai...j����ı����˷������������Сֵ

void computechain(int *p,int len,int m[50][50],int s[50][50])
{
    int i,j,k,t;
    for(i=0;i<=len;++i) m[i][i] = 0;
    for(t=2;t<=len;t++){                //��ǰ���˾���ĳ���
        for(i=1;i<=len-t+1;i++){       //�ӵ�һ����ʼ���𣬼��㳤��Ϊt�����ٴ���
            j=i+t-1;                        //����Ϊtʱ������һ��Ԫ��
            m[i][j] = 100000;         //��ʼ��Ϊ������
            for(k=i;k<=j-1;k++){        //Ѱ�����ŵ�kֵ��ʹ�÷ֳ�������k��i��j-1֮��
                int temp = m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j];
                if(temp < m[i][j]){
                    m[i][j] = temp;     //��¼�µ�ǰ����С����
                    s[i][j] = k;            //��¼��ǰ������λ�ã�������ı��
                }
            }
        }
    }
}

int main()
{
    int N;
    cin>>N;  //N������
    int *p=new int[N+1];
    for(int i=0;i<N+1;i++) cin>>p[i];  //N+1������
    for(int i=0;i<50;i++) m[50][50]=0;  //��ʼ��
    computechain(p,N+1,m,s);   //�� i �� j �ľ���������С�˷���������ֵ�����
    cout<<m[1][N]<<endl;
    return 0;
}



