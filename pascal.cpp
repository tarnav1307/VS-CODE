#include<iostream>
using namespace std;
int fact(int n){
    int factorial = 1;
    if( n<= 0){
        return 1;
    }
    for(int i = 1 ; i <= n ; i++){
        factorial*=i;
    }
    return factorial;
}
int main(){
    int n;
    cout<<"Enter the no. of rows"<<endl;
    cin>>n;
    for(int i = 0 ; i<n;i++){
        for(int j = 0 ; j<=i;j++){
            float a = fact(i)/(fact(j)*fact(i - j));
            cout<<a<<' ';
        }
        cout<<endl;
    }
    return 0;
}