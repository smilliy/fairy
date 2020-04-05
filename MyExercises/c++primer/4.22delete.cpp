// delete.cpp -- using the delete operator

#include <iostream>
#include <cstring>  // or string.h

using namespace std;
char * getname(void);   // function prototype

int main()
{
    char * name;    // create pointer but no storage
    //cout << name << " : " << *name << endl;
    //cout << *name << endl;

    name = getname();   // assign address of string to name
    cout << name << " at " << (int*) name << "\n";
    delete [] name; // memory freed

    name = getname(); // reuse freed memory
    cout << name << " at " << (int*) name << "\n";
    delete [] name; // memory freed

    name = getname(); // reuse freed memory
    cout << name << " at " << (int*) name << "\n";
    delete [] name; // memory freed

    name = getname(); // reuse freed memory
    cout << name << " at " << (int*) name << "\n";
    delete [] name; // memory freed

    return 0;
}

char * getname(void)    // return pointer to new string
{
    char temp[80];  // temporary storage
    cout << "Enter last name: ";
    cin >> temp;
    char * pn = new char[strlen(temp) + 1];
    strcpy(pn, temp);   // copy string into smaller space
    return pn;  // temp lost when function ends;
}
