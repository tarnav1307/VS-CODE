#include<iostream>
using namespace std;
int fact(int n){
    if(n<=1){
        return 1;
    }
    else{
        return n*fact(n-1);
    }
    
}
int main(){
   int n;
   cout<<"Enter the no. of rows : ";
   cin>>n;
   for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
        int ans=(fact(i)/(fact(i-j)*fact(j)));
        if(j<=i){
        cout<<ans<<" ";
        }
    }
    cout<<endl;
   }

}