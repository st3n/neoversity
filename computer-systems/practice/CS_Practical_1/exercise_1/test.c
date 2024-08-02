#include <stdio.h>
#include <stdbool.h>
 
int main()
{
    int num;
 
    // Input the integer
    printf("Enter the integer: ");

    scanf("%d", &num);

    bool isEven = false;
    if(num % 2 == 0)
        isEven = true;

    if(isEven)
        printf("Number is even!");
    else
        printf("Number is odd!");
    
    scanf("%d", &num);
    return 0;
}