#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

string ciphertext(string text, int k);
bool only_digits(string s);

int main(int argc, string argv[]) 
{
    /*if argument != 1 and not digit on command line
        print error message
        exit and return 1
    */
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //convert first arg (key) to an int modulo 26
    int key = atoi(argv[1]) % 26;

    //prompt user to enter a text
    string plaintext = get_string("plaintext: ");

    //call a function to cipher the text with the key
    string textciphered = ciphertext(plaintext, key);

    printf("ciphertext: %s\n", textciphered);
    return 0;
}

string ciphertext(string text, int k)
{
    /* rotate by k position any aplha
    text[i] est un char avec la valeur ascii
    */
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char letter = text[i];
        if (isalpha(letter) && isupper(letter)) 
        {
            if (letter + k > 90)
            {
                text[i] = text[i] - (26 - k);
            }
            else
            {
                text[i] = text[i] + k;
            }
        }
        else if (isalpha(letter) && islower(letter)) 
        {
            if (letter + k > 122)
            {
                text[i] = text[i] - (26 - k);
            }
            else
            {
                text[i] = text[i] + k;
            }
        }
    }
    return text;
}

bool only_digits(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (isdigit(s[i]))
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}