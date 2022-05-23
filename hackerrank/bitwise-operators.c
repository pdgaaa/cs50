#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k)
{
  int max_and = 0;
  int max_or = 0;
  int max_xor = 0;
  int result_and = 0;
  int result_or = 0;
  int result_xor = 0;

  for (int i = 1; i < n; i++)
  {
    for (int j = i + 1; j <= n; j++)
    {
      result_and = i & j;
      result_or = i | j;
      result_xor = i ^ j;

      if ((result_and > max_and) && (result_and < k))
      {
        max_and = result_and;
      }
      
      if ((result_or > max_or) && (result_or < k))
      {
        max_or = result_or;
      }
      
      if ((result_xor > max_xor) && (result_xor < k))
      {
        max_xor = result_xor;
      }
      //printf("%i & %i is %i; ", i, j, i & j);
      //printf("%i | %i is %i; ", i, j,  i | j);
      //printf("%i ^ %i is %i;\n", i, j, i ^ j);
    }
  }
  printf("%i\n", max_and);
  printf("%i\n", max_or);
  printf("%i\n", max_xor);
}

int main() {
  int n, k;

  scanf("%d %d", &n, &k);
  calculate_the_maximum(n, k);

  return 0;
}