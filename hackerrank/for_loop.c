#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);
  	// Complete the code.


    char array_number[10][6] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    for (int i = a; i <= b; i++)
    {
        if (i <= 9)
        {
            printf("%s\n", array_number[i]);
        }
        else if (i % 2 == 0)
        {
            printf("even\n");
        }
        else if (i % 2 == 1)
        {
            printf("odd\n");
        }
    }
  
    return 0;
}

