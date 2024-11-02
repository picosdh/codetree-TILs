#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    for(int i=0; i<=100-a; i++){
        cout << a+i << ' ';
    }
    return 0;
}