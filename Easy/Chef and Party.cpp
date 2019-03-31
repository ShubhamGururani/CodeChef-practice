#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t>0){
	    int n;
	    cin>>n;
	    int *ar = new int[n];
	    for(int i =0;i<n;i++){
	        cin>>ar[i];
	    }
	    sort(ar,ar+n);
	    int friends = 0;
	    for(int i = 0;i<n;i++){
	        if(ar[i]<=friends){
	            friends++;
	        }
	    }
	    cout<<friends<<endl;
	    delete []ar;
	    t--;
	}
	return 0;
}
