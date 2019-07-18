#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long



int32_t main() {
	// code here
	IOS;
	int t;
	cin>>t;
	int dx[]={1,0,-1,0};
	int dy[]={0,1,0,-1};
	while(t--){
	    int n,m,k;
	    cin>>n>>m>>k;
	    int ans=0;
	    int i = 0;
	    set<pair<int,int>>plants;
	    while(i<k){
	        cin>>x[i]>>y[i];
	        if(plants.find({x[i],y[i]})!=plants.end())
	            assert(0);
	        plants.insert({x[i],y[i]});
	        i++;
	    }
	    i=0;
	    while(i<k){
	        for(int j=0;j<4;j++){
	            pair<int,int>p={x[i]+dx[j],y[i]+dy[j]};
	            if(plants.find(p)==plants.end())
	                ans++;
	        }
	        i++;
	    }
	    cout<<ans<<endl;
	    
	    
	}
	
	
	return 0;
}
