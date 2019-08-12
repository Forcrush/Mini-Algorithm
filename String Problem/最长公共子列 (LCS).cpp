#include <iostream>
using namespace std;

int main(){
    int lena, lenb;
    cout<<"String A length:";
    cin>>lena;
    cout<<"String B length:";
    cin>>lenb;
    int A[lena];
    int B[lenb];
    cout<<"Input A:";
    for(int i=0;i<lena;i++) cin>>A[i];
    cout<<"Input B:";
    for(int i=0;i<lenb;i++) cin>>B[i];

    int c[lena+1][lenb+1];
    for (int i=0; i<lena + 1; i++){
        for(int j=0; j<lenb + 1; j++){
            c[i][j] = 0;
        }
    }

    int res = 0;
    for (int i=1; i<lena + 1; i++){
        for (int j=1; j<lenb + 1; j++){
            if (A[i - 1] == B[j - 1]){
                c[i][j] = c[i - 1][j - 1] + 1;
            }
            else{
                c[i][j] = max(c[i - 1][j], c[i][j - 1]);
            }
            res = max(res, c[i][j]);
        }
    }
    cout<<res;
    return 0;
}
