#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a=0;
    while(n != 0){
        int ab = n%10;
        a = a*10 + ab;
        n = n/10;
    }
    cout<<a;
    return 0;
}