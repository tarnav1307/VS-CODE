#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int a = 0;
    int i = 2;
    int c = 0;
    while(n!=0){
        int ab = n % 10;
        a = a+ab*(pow(i,c));
        n = n / 10;
        c++;
    }
    cout<<a;
    
}