#include <iostream>
#include <cstring>
#include "14.10workermi.h"

const int SIZE = 5;

int main()
{
    using std::cin;
    using std::cout;
    using std::endl;
    using std::strchr;

    Worker * loals[SIZE];

    int ct;
    for (ct = 0; ct < SIZE; ct++)
    {
        char choice;
        cout << "Enter the employee category:\n"
             << "w: waiter   s: singer   t: singing waiter    q: quit\n";
        cin >> choice;
        while (strchr("wstq", choice) == NULL)
        {
            cout << "Please enter w s t or q: ";
            cin >> choice;
        }
        if (choice == 'q')
            break;
        switch (choice)
        {
        case 'w':
            loals[ct] = new Waiter;
            break;
        case 's':
            loals[ct] = new Singer;
            break;
        case 't':
            loals[ct] = new SingingWaiter;
            break;
        }
        cin.get();
        loals[ct]->Set();
    }
    cout << "\nHere is your staff:\n";
    int i;
    for (i = 0; i < ct; i++)
    {
        cout << endl;
        loals[i]->Show();
    }
    for (i = 0; i < ct; i++)
    {
        delete loals[i];
    }
    cout << "Bye.\n";
    return 0;
}
