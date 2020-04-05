// switch.cpp -- using the switch statement

#include <iostream>

using namespace std;
void showmenu();
void report();
void comfort();

int main()
{
    showmenu();
    int choice;
    cin >> choice;
    while(choice != 5)
    {
        switch(choice)
        {
        case 1 :
            cout << " 1\a\n";
            break;
        case 2 :
            report();
            break;
        case 3 :
            cout << "The boss was in all day.\n";
            break;
        case 4 :
            comfort();
            break;
        default:
            cout << "That's not a choice.\n";
        }
        showmenu();
        cin >> choice;
    }
    cout << "bye!\n";
    return 0;
}

void showmenu()
{
    cout << R"(Please enter 1, 2, 3, 4, or 5:
1) alarm    2) report
3) alibi    4) comfort
5) quit
)";
}

void report()
{
    cout << "It's been an excellent week for business.\n"
         << "Sales are up 120%. Expense are down 35%.\n";
}

void comfort()
{
    cout << R"(Your employees think you are the finest CEO
in the industry. The board of directors think
you are the finest CEO in the industry.
)";
}
