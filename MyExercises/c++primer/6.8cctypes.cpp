// cctypes.cpp -- using the ctype.h library

#include <iostream>
#include <cctype>   // prototypes for character functions

int main()
{
    using namespace std;
    cout << "Enter text for analysis, and type @ to terminal input.\n";
    char ch;
    int whitespace {};
    int digits {};
    int chars {};
    int punct {};
    int others {};

    cin.get(ch);
    while(ch != '@')
    {
        if(isalpha(ch))
            chars++;
        else if(isspace(ch))
            whitespace++;
        else if(isdigit(ch))
            digits++;
        else if(ispunct(ch))
            punct++;
        else
            others++;
        cin.get(ch);
    }
    cout << chars << " letters, " << whitespace << " whitespace, "
         << digits << " digits, " << punct << " punctuations, "
         << others << " others.\n";
    return 0;

}
