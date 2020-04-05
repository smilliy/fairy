#include <iostream>
#include <string>
#include <cctype>
#include "14.13stacktp.h"

using std::cin;
using std::cout;

int main()
{
    Stack<std::string> st;
    char ch;
    std::string po;

    cout << "Please enter A to add a purchase order,\nP to process a P0, or Q to quit.\n";
    while(cin >> ch && toupper(ch) != 'Q')
    {
        while (cin.get() != '\n')
            continue;
        if (!isalpha(ch))
        {
            cout << '\a';
            continue;
        }
        switch (ch)
        {
        case 'A':
        case 'a':
            cout << "Enter a P0 number to add: ";
            cin >> po;
            if (st.isfull())
                cout << "Stack already full\n";
            else
                st.push(po);
            break;
        case 'P':
        case 'p':
            if (st.isempty())
                cout << "Stack already empty\n";
            else
            {
                st.pop(po);
                cout << "P0 #" << po << " popped\n";
            }
            break;
        }
        cout << "Please enter A to add a purchase order,\nP to process a P0, or Q to quit.\n";
    }
    cout << "Bye\n";
    return 0;
}
