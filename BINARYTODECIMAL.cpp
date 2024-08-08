#include<iostream> 
#include<math.h>
using namespace std;
int main(){
    int a;
    cout<<"Enter the binary no."<<endl;
    cin>>a;
    int number=0;
    int i = 0;
    while(a>0){
        int lastdig = a%10;
        number = number + lastdig*pow(2,i);
        a = a/10;
        i++;
    }
    cout<<"the no. is "<<number;
}