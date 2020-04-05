// waiting.cpp  -- using clock() in a time-delay loop

#include <iostream>
#include <ctime>    // describes clock() function, clock_t type

int main()
{
    using namespace std;
    cout << "Enter the delay time, in seconds: ";
    float secs;
    cin >> secs;
    clock_t delay = secs * CLOCKS_PER_SEC;  // convert to clock ticks
    cout << "Starting\a...\n";
    clock_t start = clock();
    while(clock() - start < delay)  // wait until time elapses
    {
        // note
    }
    cout << "Done.\a\n";
    return 0;
}
