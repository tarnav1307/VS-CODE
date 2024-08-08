#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i = 1;i<=n;i++){
        for(int j = 1; j<= n-i;j++){
            cout<<" ";
        }
        int a = i;
        for(int j = 1; j<=i;j++){
            cout<<a;
            a--;

        }
        int b= 2;
        for(int j = 1; j<i;j++){
            cout<<b;
            b++;
        }
        cout<<endl;
    }
    return 0;
}