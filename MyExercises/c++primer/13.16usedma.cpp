#include <iostream>
#include "13.14dma.h"

int main()
{
    using std::cout;
    using std::cin;
    using std::endl;

    baseDMA shirt("Protabelly", 8);
    lackDMA ballon("red", "Blimpo", 4);
    hasDMA map("Mercator", "Buffalo keys", 5);
    cout << "Displaying baseDMA object:\n";
    cout << shirt << endl;
    cout << "Displaying lackDMA object:\n";
    cout << ballon << endl;
    cout << "Display hasDMA object:\n";
    cout << map << endl;
    lackDMA ballon2(ballon);
    cout << "Result of lackDMA copy:\n";
    cout << ballon2 << endl;
    hasDMA map2;
    map2 = map;
    cout << "Result of hasDMA assignment:\n";
    cout << map2 << endl;
    return 0;
}
