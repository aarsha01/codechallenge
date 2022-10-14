#include<cstdio>
#include<iostream>
using namespace std;
int main(){
    int n,k,paid,i,order,sum=0;
    cin >>n >>k;
    for(i=0; i<n; i++){
        cin>>order;
        if(i!=k){
            sum+=order;
        }
    }
       sum=sum/2;
       cin>>paid;
       if(sum==paid){
           cout<<"Bon Appetit";
           
       } 
       else{
           cout<<paid-sum;
       }
    
}
