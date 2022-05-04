#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void) 
{
    string text = get_string("Text: ");
    int number_letters = count_letters(text);
    int number_words = count_words(text);
    int number_sentences = count_sentences(text);
    //printf("%i letters\n %i words\n %i sentences\n", number_letters, number_words, number_sentences);
    float L = ((float) number_letters / (float) number_words) * 100;
    float S = ((float) number_sentences / (float) number_words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = (int) round(index);
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");

    }
    else
    {
        printf("Grade %d\n", grade);
    }
}

int count_sentences(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char character = text[i];
        //. is 46, ! is 33, ? is 63
        if ((character == 46) || (character == 33) || (character == 63))
        {
            count++;
        }
    }
    return count;
}
int count_words(string text)
{
    //start at 1 cause we can't detect the first word
    int count = 1;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        //space char == 32
        if (isalpha(text[i]) && text[i - 1] == 32)
        {
            count++;
        }
    }
    return count;
}

int count_letters(string text)
{
    int count = 0;
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char letter = text[i];
        if ((letter >= 65 && letter <= 90) || (letter >= 97 && letter <= 122))
        {
            count++;
        }
    }
    return count;
}