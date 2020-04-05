// block.cpp -- use a block statement

#include <iostream>
int main()
{
    using namespace std;
    cout << "The Amazing Accounto will sum and average five numbers for you.\n";
    cout << "Please enter five values: \n";
    double number;
    double sum = 0.0;
    for(int i = 1; i <= 5; i++)
    {
        cout << "value " << i << ": ";
        cin >> number;
        sum += number;
    }
    cout << "Five exquisite choice indeed! They sum to " << sum << endl;
    cout << "and average to " << sum / 5 << ".\n";
    cout << "The Amazing Accounto bids you adieu!\n";
    return 0;
}
