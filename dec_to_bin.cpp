#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a = 0;
    int i = 1;
    while(n!=0){
        int ab = n % 2;
        a = a+ab*i;
        n = n / 2;
        i *= 10;
    }
    cout<<a;
    
}