#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t = 0;
	cin>>t;
	while(t>0){
	    int n = 0;
	    cin>>n;
	    int sum = 0;
	    while(n>0){
	        int a = 0,b = 0;
	        cin>>a>>b;
	        sum = sum + a - b;
	        n--;
	        }
	    cout<<sum<<endl;
	    t--;
	}
	return 0;
}
