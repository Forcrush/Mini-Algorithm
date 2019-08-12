#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"How many numbers:";
    cin>>n;
    int arr[n+1];
    cout<<"Input numbers:";
    for(int i=1;i<=n;i++) cin>>arr[i];
    int dp[n+1]={0};
    dp[1]=1;
    for(int i=2;i<=n;i++){
        int m=0;
        for(int j=1;j<i;j++){
            if(dp[j]>m && arr[i]>arr[j])
                m=dp[j];
        }
        dp[i]=m+1;
    }
    int maxlen=-1;
    for(int i=1;i<=n;i++){
        if(dp[i]>maxlen) maxlen=dp[i];
    }
    cout<<"Max length of the monotonously increasing subsequence:"<<maxlen<<endl;
    return 0;
}
