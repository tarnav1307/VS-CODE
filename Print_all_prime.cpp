#include<iostream>
using namespace std;
int main(){
    int c;
    cin>>c;
    int a=1;
    for(int i =2; i<=c ; i++){
        for(int j=2;j<i;j++){
            if(i%j!=0){
                a = 1;
            }
            else{
                a=0;
                break;
            }
        }
        if(a==1){
            cout<<i<<endl;
        }
    }
    return 0;
}