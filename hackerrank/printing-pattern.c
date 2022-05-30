#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else 
    {
        return b;
    }
}

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    
    for (int y = -(n - 1); y <= n - 1; y++)
    {      
        /* 
        -3  -2  -1  0 1 2 3 i
        4    3   2  1 2 3 4 k
        k = |i| + 1 
        */
        for (int x = -(n - 1); x <= n - 1; x++)
        {      
           printf("%d ", max(abs(x), abs(y)) + 1); 
        }
        printf("\n");
        
    }  
    return 0;
}
