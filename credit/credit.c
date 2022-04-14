#include <cs50.h>
#include <stdio.h>

int digit_extract(long ccn, int position)
{
    for (int i=0; i < position; i++)
    {
        ccn = ccn / 10;
    }
    return ccn % 10;
}

int size_card(long ccn)
{
    int size_of_card = 0;
    do
    {
        ccn = ccn / 10;
        size_of_card++;
    } while (ccn > 0);
    return size_of_card;
}

int main(void) 
{
    long credit_card_number = 0;
    int size = 0;
    int sum = 0;
    int sum1 = 0;
    int sum2 = 0;
    int first = 0;
    int second = 0;

    // get credit card number with simple size check
    do
    {
        credit_card_number = get_long("Please, enter your credit card number: ");
        size = size_card(credit_card_number);
    } while (size < 13 || size > 16);
    
    // calculate first sum, function ?
    for(int i = 1 ; i <= size ; i+=2)
    {
        int temp_digit = digit_extract(credit_card_number,i) * 2;
        if (temp_digit > 9)
        {
            int unit = temp_digit % 10;
            int dizaine = (temp_digit / 10) % 10;
            temp_digit = unit + dizaine;
        }
        sum1 = sum1 + temp_digit;
    }
    
    // calculate second sum, function ?
    for(int i = 0 ; i <= size ; i+=2)
    {
        sum2 = sum2 + digit_extract(credit_card_number,i);
    }
    
    // calculate total sum
    sum = sum1 + sum2;
    first = digit_extract(credit_card_number,size - 1);
    second = digit_extract(credit_card_number,size - 2);

    // check and find type of the card
    if ( sum % 10 != 0)
    {
        printf("INVALID SUM\n");
    }
    else if (size == 16 && (first == 5 && (second >= 1 || second <= 5)))
    {
        printf("MASTERCARD\n");
    }
    else if (size == 15 && (first == 3 && (second == 4 || second == 7)))
    {
        printf("AMEX\n");
    }
    else if ((size >= 13 && size <= 16) && first == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
