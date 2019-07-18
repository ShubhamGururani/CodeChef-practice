#include bitsstdc++.h
using namespace std;

#define IOS iossync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl n
#define int long long


pairint,intar[250005];
int32_t main() {
	//code here
	IOS;
	int t;
	cint;
	while(t--){
	    int n;
	    cinn;
	    for(int i =0;in;i++){
	        for(int j=0;jn;j++){
	            int x;
	            cinx;
	            ar[x].first = i;
	            ar[x].second= j;
	        }
	    }
        int ans=0;
	    for(int i =1;inn;i++){
	        ans+=abs(ar[i+1].first-ar[i].first)+abs(ar[i+1].second-ar[i].second);
	    }
	    coutansendl;
	}
	
	return 0;
}
