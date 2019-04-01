#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	int n , k;
	cin>>n>>k;
	bool *ar = new bool[n];
	for(int i =0;i<n;i++)
	    ar[i] = false;
	string a;
	getline(cin,a);
	//cout<<"ye discard hora :"<<a<<": yaha tak"<<endl;
	for(int i =0;i<k;i++){
	    string str;
	    cin>>str;
	    //cout<<"ye str hai :"<<(int)str[6]<<endl;
	    if(str=="CLOSEALL"){
	        for(int i =0;i<n;i++)
	            ar[i] = false;
	        cout<<0<<endl;
	    }
	    else if(str == "CLICK"){
	        int pos = 0;
	        cin>>pos;
	        //cout<<"ye pos hai :"<<pos<<endl;
	            ar[pos-1] = !ar[pos-1];
	        int count = 0;
	        for(int i =0;i<n;i++)
	            if(ar[i])
	                count++;
	        cout<<count<<endl;
	        }
	    
	}
	delete []ar;
}