#include <cs50.h>
#include <stdio.h>

int main(void) 
{
    int row;
    int height = get_int("Height: ");
    for (row=1 ; row <= height ; row++)
    {
        for (int j=1 ; j <= height - row ; j++)
        {
            printf(" ");
        }
        for (int k=1 ; k <= row ; k++)
        {
            printf("#");
        }
        printf("  ");
        for (int k=1 ; k <= row ; k++)
        {
            printf("#");
        }
        printf("\n");    
    }
}
