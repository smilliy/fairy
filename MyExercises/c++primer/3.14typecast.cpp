// typecast.cpp -- forcing type changes

#include <iostream>

int main()
{
    using namespace std;
    int auks {}, bats {}, coots {};

    // the flowing statement adds the values as double,
    // then converts the result to int
    auks = 19.99 + 11.99;

    // these statements add values as int
    bats = (int) 19.99 + (int) 11.99;   // old C syntax
    coots = int(19.99) + int(11.99);    // new C++ syntax
    cout << "auks = " << auks << ", bats = " << bats
         << ", coots = " << coots << endl;

    char ch = 'Z';
    cout << "The code for " << ch << " is "
         << int(ch) << endl;
    cout << "Yes, the code is "
         << static_cast<int>(ch)
         <<endl;
    return 0;
}
