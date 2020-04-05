// my first cpp -- display a message

#include <iostream>
#include <direct.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;


int main()
{
    char buffer[_MAX_PATH];
    getcwd(buffer, _MAX_PATH);
    cout << buffer << endl;
    freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int a = 0;
    cout << "bb";
    while (scanf("%d", &a) != EOF)
    {
        cout << a << endl;
    }
    fclose(stdin);
    cout << "aa";
    freopen("CON", "r", stdin);

    return 0;

}


