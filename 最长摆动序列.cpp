#include <iostream>
using namespace std;

int main(){
    int len;
    cout<<"String length:";
    cin>>len;
    int arr[len];
    cout<<"Input str:";
    for(int i=0;i<len;i++) cin>>arr[i];

    int up = 1;
    int down = 1;
    for (int i=1; i<len; i++){
        if (arr[i] > arr[i - 1]){
            up = down + 1;
        }
        else if (arr[i] < arr[i - 1]){
            down = up + 1;
        }
    }
    cout<<max(up, down);
    return 0;
}
