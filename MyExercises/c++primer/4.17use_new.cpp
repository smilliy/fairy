// use_new.cpp -- using the new operator

#include <iostream>

int main()
{
    using namespace std;
    int nights = 1001;
    int *pt = new int;  // allocate space for an int
    *pt = 1001;

    cout << "nights value = " << nights << ": location = " << &nights << endl;
    cout << "int " << "value = " << *pt << ": location = " << pt << endl;

    double *pd = new double;    // allocate space for double
    *pd = 10000001.0;   // store a double there

    cout << "double value = " << *pd << ": location = " << pd << endl;
    cout << "location of pointer pd: " << &pd << endl;
    cout << "size of pt = " << sizeof(pt) << ": size of *pt = " << sizeof(*pt) << endl;
    cout << "size of pd = " << sizeof(pd) << ": size of *pd = " << sizeof(*pd) << endl;
    return 0;
}
