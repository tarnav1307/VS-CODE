#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main(){
    int n;
    cin>>n;
    char l[]= {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
    string a = "";
    int i = 1;
    while(n!=0){
        int ab = n % 16;
        a = a + l[ab];
        n = n / 16;
        i *= 10;
    }
    reverse(a.begin(),a.end());
    cout<<a;
    
}