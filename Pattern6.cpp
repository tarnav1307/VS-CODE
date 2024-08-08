#include <iostream>
using namespace std;
int main()
{
    int n = 4;
    for (int i = 1; i <= n; i++)
    {
        char c = 'a' + n - i;
        for (int j = 1; j <= n; j++)
        {
            if (j <= i)
            {
                cout << c << ' ';
                c++;
            }
        }
        cout << endl;
    }
}