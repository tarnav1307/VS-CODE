#include <iostream>
using namespace std;
int main()
{
    int n = 4;
    char c = 'a';
    for (int i = 1; i <= n; i++)
    {
        char c = 'a'+i-1;
        for (int j = 1; j <= n; j++)
        {
            
            {
                cout << c << ' ';
                c++;
            }
        }
        cout << endl;
    }
}