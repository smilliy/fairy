// arrstruc.cpp -- an array of structures

#include <iostream>

struct inflatable
{
    char name[20];
    float volumn;
    double price;
};

int main()
{
    using namespace std;
    inflatable guests[2] =  // initializing an array of structs
    {
        {"Bambi", 0.5, 21.99},  // first structure in array
        {"Godzilla", 2000, 565.99}  // next structure in array
    };

    cout << "The guests " << guests[0].name << " and " << guests[1].name
    << "\nhave a combined volume of " << guests[0].volumn + guests[1].volumn
    << " cubic feet.\n";
    return 0;
}
