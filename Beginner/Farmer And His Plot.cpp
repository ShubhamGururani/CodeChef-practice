#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int gcd(int a,int b)
{
	if (a%b==0)
		return b;
	return gcd(b,a%b);
}
int main() {
	// code here
	int t;
	cin>>t;
	while(t--){
	    int n,m;
	    cin>>n>>m;
	    int gc = gcd(n,m);
	    int totalArea = m*n;
	    cout<<totalArea/(gc*gc)<<endl;
	}
	return 0;
}
