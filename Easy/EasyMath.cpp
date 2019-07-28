#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define watch(x) cout << #x << " is " << x << endl;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int sumOfDigit(int num){
    int sum = 0;
    while(num>0){
        sum+=num%10;
        num/=10;
    }
    return sum;
}

int main() {
	// code here
	IOS;
	int t;
	cin>>t;
	while(t--){
	    int num;
	    cin>>num;
	    int ar[num];
	    for(int i =0;i<num;i++)
	        cin>>ar[i];
	    int maxSum=0;
	    for(int i = 0;i<num;i++){
	        for(int j=i+1;j<num;j++){
	            int temp=sumOfDigit(ar[i]*ar[j]);
	            if(temp>maxSum)
	                maxSum= temp;
	        }
	    }
	    cout<<maxSum<<endl;
	}
	
	return 0;
}
