#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a == 0){
        if (b < 19){
            cout << "BOY";
        }
        else{
            cout << "MAN";
        }
    }
    else{
        if (b < 19){
            cout << "GIRL";
        }
        else{
            cout << "WOMAN";
        }
    }
    return 0;
}