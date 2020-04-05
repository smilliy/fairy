// exceed.cpp -- exceeding some integer limits

#include <iostream>
#define ZERO 0  //makes ZERO symbol for 0 level
#include <climits>

int main()
{
    using namespace std;
    short sam = SHRT_MAX;   // initialize a varialbe to max value
    unsigned short sue = sam;   //okay if variable sam already defined

    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited." << endl
         << "Add $1 to each account." << endl << "Now ";
    sam = sam + 1;
    sue = sue + 1;
    cout << "Sam has " << sam << " dollars and Sue has " << sue
         << "dollars deposited.\nPoor Sam!" << endl;

    sam = ZERO;
    sue = ZERO;
    cout << "Sam has " << sam <<" dollars and Sue has " << sue;
    cout << "Take $1 form each account." <<endl << "Now ";
    sam = sam -1;
    sue = sue -1;
    cout << "Sam has " << sam << " dollars and Sue has " << sue;
    cout << " dollars deposited." << endl << "Lucky Sue." << endl;
    return 0;
}
