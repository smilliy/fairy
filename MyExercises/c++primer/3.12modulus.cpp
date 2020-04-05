// modulus.cpp -- uses % operator to convert lbs to stone

#include <iostream>

int main()
{
    using namespace std;
    const int Lbs_per_stn = 14;
    int lbs {};

    cout << "Enter your weight in pounds: ";
    cin >> lbs;
    int stone = lbs / Lbs_per_stn;  // whole stone;
    int pounds = lbs % Lbs_per_stn; // remainder in pounds
    cout << lbs << " ponuds are " << stone << " stone, "
         << pounds << " pounds." << endl;
    return 0;
}
