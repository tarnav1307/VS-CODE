#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"enter the no. of rows";
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(j<=i){
                cout<<"* ";
            }
            else
                continue;
        }
        cout<<endl;
    }
    return 0;
}