#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n; j++){
            if(j%2 == 1){
                if(i == 1){
                    printf("* ");
                }
                else{
                    printf("  ");
                }
            }
            else{
                if(i>j){
                    printf("  ");
                }
                else{
                    printf("* ");
                }
            }
        }
        printf("\n");
    }
    return 0;
}