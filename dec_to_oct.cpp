#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a = 0;
    int i = 1;
    while(n!=0){
        int ab = n % 8;
        a = a+ab*i;
        n = n / 8;
        i *= 10;
    }
    cout<<a;
    
}