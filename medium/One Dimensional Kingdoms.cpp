#include <bits/stdc++.h>
using namespace std;

int ar[2001];
int main(){
    int t = 0;
    cin>>t;
    while(t>0){
        int n = 0;
        cin >> n;
        for (int i =0 ;i<2000;i++){
            ar[i] =-1;
        }
        for (int i =0 ;i < n ;i++){
            int a = 0,b = 0;
            cin>>a>>b;
            if(ar[b]<a)
                ar[b] = a;
        }
        int count= 0;
        int val= -1;
        for (int i = 0 ; i < 2001 ; i++){
            if( val < ar[i] ){
                count++;;
                val=i;
            }
        }
        cout<<count<<endl;
        t--;
    }
    return 0;
}
