// structur.cpp -- a simple structure

#include <iostream>

struct inflatable   // structure declaration
{
    char name[20];
    float volumn;
    double price;
};

int main()
{
    using namespace std;
    inflatable guest =
    {
        "Glorious Gloria",  // name value
        1.88,   // volume value
        29.99   // price value
    };  // guest is a structure variable of type inflatable
    // It's initialized to the indicated values
    inflatable pal =
    {
        "Audacious Arthur",
        3.12,
        32.99
    };  // pal is a second variable of type inflatable
    // NOTE: some implementations require using
    // static inflatable guests =

    cout << "Expand your guest list with " << guest.name << " and " << pal.name << "!\n";
    // pal.name is the name member of the pal variable
    cout << "You can have both for $" << guest.price + pal.price << "!\n";
    return 0;
}
