#include <bits/stdc++.h>
using namespace std;
map<long,long> m;

long factorize(long num){
    if(num < 5)
        return num;
    if(m.find(num) != m.end())
        return m[num];
    long p1 = factorize(num/2);
     //cout<<"p1 hai"<<p1<<endl;
    long p2 = factorize(num/3);
     //cout<<"p2 hai"<<p2<<endl;
    long p3 = factorize(num/4);
     //cout<<"p3 hai"<<p3<<endl;
        //cout<<"return hua "<<num<<endl;
    return (m[num] = max(num,p1+p2+p3));
}
int main() {
	// your code goes here
	long a;
	while(cin>>a){
	long ans = factorize(a);
	cout<<ans<<endl;
	}
	return 0;
}
