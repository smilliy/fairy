//  lotto.cpp -- probability of winning

#include <iostream>

long double probability(unsigned int numbers, unsigned int picks);

int main()
{
    using namespace std;
    double total, choices;
    cout << "Enter the total number of choices on the game card and \n"
         "the number of picks allowed:\n";
    while((cin >> total >> choices) && choices <= total)
    {
        cout << "You have one chance in " << probability(total, choices)
             << " of winning.\n";
        cout << "Next two numbers (q to quit): ";
    }
    cout << "Bye\n";
    return 0;
}

long double probability(unsigned int numbers, unsigned int picks)
{
    long double result = 1.0;
    long double n;
    unsigned p;

    for(n = numbers, p = picks; p > 0; n--, p--)
        result = result * n / p;
    return result;
}
