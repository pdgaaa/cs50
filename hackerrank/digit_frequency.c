#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char *s;
    s = malloc(1024 * sizeof(char));
    //char *counting_array;
    //counting_array = malloc(1024 * sizeof(char));
    //init an array with 0
    int counting_array[1024];
    for (int i= 0; i < 1024; i++)
    {
        counting_array[i] = 0;
    }
    
    //get input
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);

    //count digit
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isdigit(s[i]))
        {
            counting_array[s[i]] += 1;
        }

    }
    
    //print digit frequency
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        
    }
    return 0;
}
