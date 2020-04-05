// dowhile.cpp

#include <iostream>

int main()
{
    using namespace std;
    int n;

    cout << "Enter numbers in the range 1-10 find my favorite number\n";
    do
    {
        cin >> n;   // execute body
    }
    while(n != 7);      // then test
    cout << "yes, 7 is my favorite.\n";
    for(int x :{3, 5, 6, 10})
    {
        cout << x << ",";
    }
    cout << endl;
    return 0;
}
