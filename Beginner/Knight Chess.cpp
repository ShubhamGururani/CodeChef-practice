#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t = 0;
	cin>>t;
	while(t>0){
	    int n = 0;
	    cin>>n;
	    int **ar = new int *[n];
	    for(int i =0;i<n;i++){
	        ar[i] = new int [2];
	        cin>>ar[i][0]>>ar[i][1];
	    }
	    int kx = 0,ky=0;
	    cin>>kx>>ky;
	    bool checkMate = true;
	    for(int i=-1;i<=1;i++)
        {
            for(int j=-1;j<=1;j++)
            {
                if(i==0 && j==0)
                    continue;
                int kxMove=kx+i,kyMove=ky+j;
                bool check = false;
                for(int i=0;i<n;i++)
                    if((abs(kxMove-ar[i][0])==2 && abs(kyMove-ar[i][1])==1) ||(abs(kxMove-ar[i][0])==1 && abs(kyMove-ar[i][1])==2)){
                        check=true;
                        break;
                    }
                    if(!check)
                    checkMate = false;
            }
        }
        if(checkMate)
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;
	    t--;
	}
	
	return 0;
}
