#include <bits/stdc++.h>
using namespace std;
int main(){
    int n,k,i,j;
    int count=0;
    cin>>n>>k;
    vector<int>arr(n);
   
    for(i=0; i<n; i++){
      cin>>arr[i];
    }
    for(i=0; i<n-1; i++){
        for(j=0;j<n; j++){
            if(i<j){
            if((arr[i]+arr[j])%k==0)
            count++;
            }
        }
    }
    cout<<count;
    return 0;
}
