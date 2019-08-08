#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define watch(x) cout << #x << " is " << x << endl;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
	// code here
	IOS;
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    ll sumA=0;
	    ll oddA=0;
	    for(int i =0;i<n;i++){
	        int temp;
	        cin>>temp;
	        sumA+=temp;
	        if(temp%2==1){
	            ++oddA;
	            sumA-=1;
	        }
	    }
	    ll sumB=0;
	    ll oddB=0;
	    for(int i =0;i<n;i++){
	        int temp;
	        cin>>temp;
	        sumB+=temp;
	        if(temp%2==1){
	            ++oddB;
	            sumB-=1;
	        }
	    }
	    ll avg = (sumA+sumB)/2;
	    avg+=min(oddB,oddA);
	    cout<<avg<<endl;
	}
	
	return 0;
}
