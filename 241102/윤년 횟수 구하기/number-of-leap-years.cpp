#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int a;
    int cnt = 0;
    scanf("%d", &a);
    for (int i = 1; i <= a; i++){
        if (i%4 == 0){
            if (i%25 == 0){
                if (i%400 != 0){
                    continue;
                }
                else{
                    cnt++;
                }
            }
            else{
                cnt++;
            }
        }
    }
    printf("%d", cnt);
    return 0;
}