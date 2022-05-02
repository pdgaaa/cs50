#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);

int main(void) 
{
    string text = get_string("Text: ");
    int number_letters = count_letters(text);
    int number_words = count_words(text);
    printf("%i letters\n %i words\n", number_letters, number_words);
}

int count_words(string text)
{
   int count = 0;
   for (int i = 0, n = strlen(text); i < n; i++)
   {
       char letter = text[i];
       //space char == 32
       if (isalpha(text[i]) && text[i-1] == 32)
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

