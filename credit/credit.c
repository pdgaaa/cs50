#include <cs50.h>
#include <stdio.h>

int digit_extract(long credit_card_number, int position);
int number_of_digits(long credit_card_number);
int add(long credit_card_number, int size, int n);
string card_type(long credit_card_number, int size, int sum);

enum CardType {
    Mastercard,
    Amex,
    Visa,
    Invalid
};


int main(void) 
{
    long credit_card_number = 0;

    // get credit card number with simple size check
    do
    {
        credit_card_number = get_long("Please, enter your credit card number: ");
        int size = number_of_digits(credit_card_number);
    } while (size < 13 || size > 16);
    
    //check and find type of card
    enum CardType card_type = card_type(credit_card_number);
    printf("%s\n", card_type_to_string(card_type));
}

string card_type_to_string(enum CardType type)
{
    switch (type)
    {
    case Mastercard:
        return "MaSTERCARD";
    case Visa:
        return "VISA";
    }
    return "";
}

enum CardType card_type(long credit_card_number)
{
    int size = number_of_digits(credit_card_number);
    int sum = checksum(credit_card_number);

    //get first and second digit
    int first = digit_extract(credit_card_number,size - 1);
    int second = digit_extract(credit_card_number,size - 2);

    // check and find type of the card
    // replace 16 by a var, like master_card_size, 15 by amex_size ?
    if ( sum % 10 != 0)
    {
        return Invalid;
    }
    else if (size == 16 && (first == 5 && (second >= 1 || second <= 5)))
    {
        return Mastercard;
    }
    else if (size == 15 && (first == 3 && (second == 4 || second == 7)))
    {
        return Amex;
    }
    else if ((size >= 13 && size <= 16) && first == 4)
    {
        return Visa;
    }
    else
    {
        return Invalid;
    }
}

int digit_extract(long credit_card_number, int position)
{
    for (int i=0; i < position; i++)
    {
        credit_card_number = credit_card_number / 10;
    }
    return credit_card_number % 10;
}

int number_of_digits(long credit_card_number)
{
    int digits_count = 0;
    do
    {
        credit_card_number = credit_card_number / 10;
        digits_count++;
    } while (credit_card_number > 0);
    return digits_count;
}


int card_number_checksum(long credit_card_number)
{
    int size = number_of_digits(credit_card_number);
    int checksum = 0;

    // checksum is computed by summing 2 components

    // first component: ...
    for(int i = 1; i < size; i+=2)
    {
        int digit_doubled = 2 * digit_extract(credit_card_number, i);
        checksum += digit_extract(digit_doubled, 0) + digit_extract(digit_extract, 1);
    }

    // second component: ...
    for(int i = 0; i < size; i+=2)
    {
        checksum += digit_extract(credit_card_number, i);
    }

    return checksum;
}

int add(long credit_card_number, int size, int n)
{
    int s = 0;
    for(int i = n ; i <= size ; i+=2)
    {
        int temp_digit = digit_extract(credit_card_number,i) * (n + 1);
        if (temp_digit > 9)
        {
            int unit = temp_digit % 10;
            int dizaine = (temp_digit / 10) % 10;
            temp_digit = unit + dizaine;
        }
        s = s + temp_digit;
    }
    return s;
}