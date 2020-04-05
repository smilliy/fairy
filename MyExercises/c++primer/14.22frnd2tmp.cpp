#include <iostream>

using std::cout;
using std::endl;

template <typename T>
class hasFriend
{
private:
    T item;
    static int ct;
public:
    hasFriend(const T & i) : item(i)
    {
        ct++;
    }
    ~hasFriend()
    {
        ct--;
    }
    friend void counts();
    friend void reports(hasFriend<T> &);
    // friend void reports(hasFriend<double> &);
};

template<typename T> int hasFriend<T>::ct = 0;

void counts()
{
    cout << "int count: " << hasFriend<int>::ct << "; ";
    cout << "double count" << hasFriend<double>::ct << endl;
}

void reports(hasFriend<int> & hf)
{
    cout << "HasFriend<int>: " << hf.item <<endl;
}

void reports(hasFriend<double>& hf)
{
    cout << "HasFriend<double>: " << hf.item << endl;
}

int main()
{
    cout << "No objects declared: ";
    counts();
    hasFriend<int> hfi1(10);
    cout << "After hfi1 declared: ";
    counts();
    hasFriend<int> hfi2(20);
    cout << "After hfi2 declared: ";
    counts();
    hasFriend<double> hfdb(10.5);
    cout << "After hfdb declared: ";
    counts();
    reports(hfi1);
    reports(hfi2);
    reports(hfdb);
    return 0;
}
