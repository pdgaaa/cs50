#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int first_int = 0;
    int second_int = 0;
    float first_float = 0.0;
    float second_float = 0.0;
    
    scanf("%d %d", &first_int, &second_int);
    scanf("%f %f", &first_float, &second_float);
    
    printf("%d %d\n", first_int + second_int, first_int - second_int);
    printf("%.1f %.1f\n", first_float + second_float, first_float - second_float);
    
    return 0;
}
