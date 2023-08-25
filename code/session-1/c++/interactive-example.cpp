#include <iostream>
#include <string>
using namespace std;

int main() {
  int high,low;
  string state;
  low = 0;
  cin >> high;
  do {
    int mid;
    mid = (low+high) / 2;
    cout << mid << endl << flush;
    cin >> state;
    if(state.compare("higher") == 0) {
      low = mid +1;
    } else if(state.compare("lower") ==0 ){
      high = mid - 1;
    }
  }while (state.compare("correct") != 0);
  return 0;
}