// outfile.cpp -- writting to a filebuf

#include <iostream>
#include <fstream>  // for file I/O

int main()
{
    using namespace std;

    char automobiles[50];
    int year;
    double a_price;
    double d_price;

    ofstream outFile;   // create object for output
    outFile.open("carinfo.txt");    // associate with a file

    cout << "Enter the make and modle of automobile: ";
    cin.getline(automobiles, 50);
    cout << "Enter the model year: ";
    cin >> year;
    cout << "Enter the original asking price: ";
    cin >> a_price;
    d_price = 0.913 * a_price;

    // display information on screen with cout
    cout << fixed;
    cout.precision(2);
    cout.setf(ios_base::showpoint);
    cout << "Make and model: " << automobiles << endl;
    cout << "Year: " << year << endl;
    cout << "Was asking $" << a_price << endl;
    cout << "Now asking $" << d_price << endl;

    // now do exact same things using outFile insted of cout
    outFile << fixed;
    outFile.precision(2);
    outFile.setf(ios_base::showpoint);
    outFile << "Make and model: " << automobiles << endl;
    outFile << "Year: " << year << endl;
    outFile << "Was asking $" << a_price << endl;
    outFile << "Now asking $" << d_price << endl;

    outFile.close();    // done with file
    return 0;
}
