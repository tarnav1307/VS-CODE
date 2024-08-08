#include<iostream>
using namespace std;

int addbinary(int a, int b){
    int ans=0;
    int carry=0;
    int i=1;
    while(a>=0 || b>=0){
        if(a%2==0 && b%2==0){
            ans += ((a%2)+(b%2)+carry)*i;
            carry=0;
        }
        else if((a%2==1 && b %2 == 0)||(a%2==0 && b %2 == 1)){
               if(carry == 0){
                ans += ((a%2)+(b%2)+carry)*i;
                carry = 0;
               } 
               else{
                ans += 0*i;
                carry=1;
               }
        }
        else if((a%2==1 && b %2 == 1)){
            if(carry == 0){
                ans += 0*i;
                carry = 1;
               } 
               else{
                ans += 1*i;
                carry=1;
               }
        }
        i*=10;
        a/=10;
        b/=10;
    }
    cout<<ans;
    return 0;
}
int main(){
    cout<<addbinary(11011,10010);
    return 0;
}