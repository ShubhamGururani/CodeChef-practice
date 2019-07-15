#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	// code here
	int t;
	cin>>t;
	while(t--){
	    ll l;
	    cin>>l;
	    string s;
	    char ch;
	    cin>>s>>ch;
	    ll temp=-1;
	    ll ans = l*(l+1)/2;
        for(int i = 0;i<l;i++){
            if(s[i]==ch){
                ll sub = i-temp-1;
                ans-=sub*(sub+1)/2;
                temp = i;
            }
        }
        if(temp<l-1){
            ll sub = l-1-temp;
            ans-=sub*(sub+1)/2;
        }
        cout<<ans<<endl;    
	}
	
	
	return 0;
}
