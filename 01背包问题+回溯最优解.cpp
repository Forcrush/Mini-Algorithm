#include <iostream>
using namespace std;


int s[20][1000]={0}; //存储解空间，最多20种物品，最大容量1000
int n,c;  // n items  | c total capicity
int w[20];  // w weights
int v[20];  // v values
int tra[20]; // 0表示未用 1表示被用

void printarray(){  // 打印数据存储结果
    for(int i=0;i<=n;i++){
        for(int j=0;j<=c;j++) cout<<s[i][j]<<" ";
        cout<<endl;
    }
}

void traceback(){
    for(int i=n;i>1;i--){
        if(s[i][c]==s[i-1][c]) tra[i]=0;
        else{
            tra[i]=1;
            c-=w[i];
        }
    }
    tra[1]=(s[1][c]>0)?1:0;
    cout<<"Optimal plan(Which item):"<<endl;
    for(int k=1;k<=n;k++){
        if(tra[k]==1) cout<<k<<"th  ";
    }
}

int main(){
    cout<<"How many kinds of items(less than 20):";
    cin>>n;
    cout<<"The total capacity of knapsack(less than 1000):";
    cin>>c;
    cout<<"weight of each item:";
    for(int i=1;i<=n;i++) cin>>w[i];
    cout<<"value of each item:";
    for(int i=1;i<=n;i++) cin>>v[i];

    for(int i=1;i<=n;i++){
        for(int j=1;j<=c;j++){
            if(j<w[i]) s[i][j]=s[i-1][j];
            else s[i][j]=max(s[i-1][j],s[i-1][j-w[i]]+v[i]);
        }
    }
    cout<<"Optimal sol:"<<s[n][c]<<endl;
    printarray();
    traceback();
    return 0;
}


