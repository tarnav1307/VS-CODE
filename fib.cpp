#include<iostream>
using namespace std;
int fib(int n){
    int a = 0, b = 1,c =0;
    for(int i = 0;i<n;i++){
        cout<<a<<endl;
        c = a + b;
        a = b;
        b = c;
        
    }
    
}
int main(){
    int n;
    cin>>n;
    cout<<endl;
    fib(n);
    return 0;
}
