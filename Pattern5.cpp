#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter the no. of rows";
    cin>>n;
    char row='A';
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(j<=i){
                cout<<row<<" ";
                row++;
            }
            else
                continue;
        }
        cout<<endl;
        
    }
    return 0;
}