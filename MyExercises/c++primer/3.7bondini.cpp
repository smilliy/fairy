// bondini.cpp -- using escape sequences

#include <iostream>

int main()
{
    using namespace std;
    cout << "\aOperation \"HyperHype\" is now activated!\n";
    cout << "Enter your agent code:_______\b\b\b\b\b\b\b";
    long long code;
    cin >> code;
    cout << "\aYou entered " << code << "...\n";
    cout << "\aCode verified! Proceed with plan Z31!\n";
    cout << "let them eat g\u00E2teau" << endl;;

    wchar_t bob = L'P'; // a wide-character constant
    wcout << L"tall" << endl;   // outputing a wide-character string
    wcout << bob;
    return 0;
}
