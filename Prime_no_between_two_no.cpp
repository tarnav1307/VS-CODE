#include<iostream>
using namespace std;
int prime(int a,int b){
    int g,s;
    if (a>=b){
        g = a;
        s = b;
    }
    else{
        g = b;
        s = a;
    }
    int l = 0;
    for(int i = s;i<=g;i++){
        for(int j=2;j<i;j++){
            if(i%j==0){
                l = 1;
                break;
            }
        }
        if(l == 0){
            cout<<i<<endl;
        }
        l=0;
    }
}
int main(){
    int a,b;
    cout<<"enter two no."<<endl;
    cin>>a>>b;
    prime(a,b);
    return 0;
}