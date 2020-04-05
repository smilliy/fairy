// instr2.cpp -- reading more than one string

#include <iostream>

int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize] {};
    char dessert[ArSize] {};

    cout << "Enter your name:\n";
    cin.getline(name, ArSize);  // reads through new line
    cin.clear();
    cin.sync();
    cout << "Enter your favorite dessert:\n";
    cin.getline(dessert, ArSize);
    cin.ignore(1024, '\n');
    cout << "I have some delicious " << dessert
         << " for you, " << name << ".\n";
    return 0;
}
