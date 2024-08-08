#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    for(int i = 1 ; i<= n;i++){
        int a = 1;
        for(int j = n; j>=i ; j--){
            cout<<a;
            a++;
        }
        cout<<endl;
    }
    return 0;
}