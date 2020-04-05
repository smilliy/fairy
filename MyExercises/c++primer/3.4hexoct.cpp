// hexoct2.cpp -- shows hex and octal literals

#include <iostream>

int main()
{
    using namespace std;
    int chest = 42; // decimal integer literal
    int waist = 42;   // hexadecimal integer literal
    int inseam = 42;   // octal integer literal

    cout << "Monsieur cuts a striking figure!\n";
    cout << "Chest = " << chest << " (42 in decimal)\n";
    cout << hex;    // manipulator for changing number base
    cout << "waist = " << waist << " (0x42 in hex)\n";
    cout << oct;    // manipulator for changing number base
    cout << "inseam = " << inseam << " (042 in octal)\n";
    return 0;
}
