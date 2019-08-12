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
    dp[1]=arr[1];
    for(int i=2;i<=n;i++){
        if(dp[i-1]<0) dp[i]=arr[i];
        else dp[i]=dp[i-1]+arr[i];
    }
    int maxsum=-100000;
    for(int k=1;k<=n;k++){
        if(dp[k]>maxsum) maxsum=dp[k];
    }
    cout<<"Maxsum:"<<maxsum<<endl;
    return 0;
}
