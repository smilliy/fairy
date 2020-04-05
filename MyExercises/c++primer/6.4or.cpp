// or.cpp -- using the logical OR operator

#include <iostream>

int main()
{
    using namespace std;
    cout << R"(This program may reformat your hard disk
and desk all your data.
"Do you wish to continue? <y/n>")";
    char ch;
    cin >> ch;
    if (ch == 'y' || ch == 'Y')
        cout << "You were warned!\a\a\n";
    else if (ch == 'n' || ch == 'N')
        cout << "A wise choice ... bye\n";
    else
        cout << R"(That wasn't a y or n! Apparently you
can not follow instructions, so I'll trash your disk anyway.\a\a\a
)";
    return 0;
}
