#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	// code here
	int t;
	scanf("%d",&t);
	while(t--){
	    int total,chains;
	    scanf("%d%d",&total,&chains);
	    int ar[chains];
	    for(int i =0;i<chains;i++)
	        scanf("%d",&ar[i]);
	    sort(ar,ar+chains);
	    int sum = 0;
	    int x;
	    for(int i = 0;i<chains;i++){
	        sum += ar[i]+1;
	        if(sum>=chains){
	            x = i;
	            break;
	        }
	    }
	    cout<<chains - x -1<<endl;
	}
	
	
	return 0;
}
