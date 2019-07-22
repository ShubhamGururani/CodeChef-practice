#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long


pair<int,int>ar[250005];
int32_t main() {
	// code here
	IOS;
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    for(int i =0;i<n;i++){
	        for(int j=0;j<n;j++){
	            int x;
	            cin>>x;
	            ar[x].first = i;
	            ar[x].second= j;
	        }
	    }
        int ans=0;
	    for(int i =1;i<n*n;i++){
	        ans+=abs(ar[i+1].first-ar[i].first)+abs(ar[i+1].second-ar[i].second);
	    }
	    cout<<ans<<endl;
	}
	
	return 0;
}
