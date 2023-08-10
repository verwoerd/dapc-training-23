#include <iostream>
using namespace std;

signed main() {
    long double x, y;
    cout << setprecision(20);
    cin >> x >> y;
    cout << (1/(1-x/100)-1)/(1/(1-y/100)-1) << endl;
    return 0;
}
