#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll maxMid(int ar[],int n){
    ll currSum = 0;
    ll maxTillNow = INT_MIN;
    for(int i  = 0;i<n;i++){
        currSum += ar[i];
        if(maxTillNow < currSum)
            maxTillNow = currSum;
        if(currSum<0)
            currSum = 0;
    }
    return maxTillNow;
}
ll maxSum(int ar[],int n,int k){
    ll maxMiddle = maxMid(ar,n);
    if( k ==1)
        return maxMiddle;
    ll currLeftSum = 0,currRightSum = 0;
    ll maxLeftSum = INT_MIN,maxRightSum = INT_MIN;
    for(int i  = 0;i<n;i++){
        currLeftSum += ar[i];
        maxLeftSum = max(currLeftSum,maxLeftSum);
    }
    ll totalSum = currLeftSum;
    for(int i =n-1;i>=0;i--){
        currRightSum += ar[i];
        maxRightSum = max(maxRightSum,currRightSum);
    }
    ll ans;
    if(totalSum<0)
        ans = max(maxLeftSum+maxRightSum,maxMiddle);
    else
        ans = max(maxRightSum+maxLeftSum+(totalSum*(k-2)),maxMiddle);
    return ans;
}

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int ar[n];
        for(int i  = 0;i<n;i++)
            cin>>ar[i];
        cout<<maxSum(ar,n,k)<<endl;
    }
    return 0;
}
