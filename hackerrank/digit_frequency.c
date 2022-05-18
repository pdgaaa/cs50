#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <cs50.h>

int main() {

    //init an array with 0
    int counting_array[1024];
    for (int i= 0; i < 1024; i++)
    {
        counting_array[i] = 0;
    }
    
    //get input
    string input = get_string("Input: ");

    //count digit
    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (isdigit(input[i]))
        {
            //input[i] is a char containing the ascii value
            //convert ascii digit value to an int by substract the ascii value of 0
            int digit = input[i] - '0';
            //+1 to the value of the digit index
            counting_array[digit] += 1;
        }
    }
    
    //print digit frequency
    for (int i = 0; i <= 9; i++)
    {
        printf("%i ", counting_array[i]);
    }
    return 0;
}