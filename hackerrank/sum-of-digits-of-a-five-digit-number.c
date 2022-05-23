#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    int sum = 0;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    do
    {
        sum = sum + (n % 10);
        n = n / 10;
    }
    while (n != 0);
    
    printf("%i", sum);
    return 0;
}
