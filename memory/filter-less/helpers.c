#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    /*for (int i = 0; i < 100 ; i++)
    {
        printf("blue %i green %i red %i\n", image[0][i].rgbtBlue, image[0][i].rgbtGreen, image[0][i].rgbtRed);
    }
    */
   for (int y = 0; y < height; y++)
   {
       for (int x = 0; x < width; x++)
       {
           double average_rgb = round((image[y][x].rgbtBlue + image[y][x].rgbtGreen + image[y][x].rgbtRed) / 3.0);
           image[y][x] = (RGBTRIPLE) {.rgbtBlue = (BYTE) average_rgb, .rgbtGreen = (BYTE) average_rgb, .rgbtRed = (BYTE) average_rgb};
       }
   }
}

BYTE clamp(double value)
{
    if (value > 255)
    {
        value = 255;
    }
    return (BYTE) value;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
   for (int y = 0; y < height; y++)
   {
       for (int x = 0; x < width; x++)
       {
           double sepiaRed = round(.393 * image[y][x].rgbtRed + .769 * image[y][x].rgbtGreen + .189 * image[y][x].rgbtBlue);
           double sepiaGreen = round(.349 * image[y][x].rgbtRed + .686 * image[y][x].rgbtGreen + .168 * image[y][x].rgbtBlue);
           double sepiaBlue = round(.272 * image[y][x].rgbtRed + .534 * image[y][x].rgbtGreen + .131 * image[y][x].rgbtBlue);
           image[y][x] = (RGBTRIPLE) {.rgbtBlue = clamp(sepiaBlue), .rgbtGreen = clamp(sepiaGreen), .rgbtRed = clamp(sepiaRed)};
       }
   }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   for (int y = 0; y < height; y++)
   {
       for (int x = 0; x < (width / 2); x++)
       {
          RGBTRIPLE pixel_temp = image[y][x];
          image[y][x] = image[y][width - 1 - x];
          image[y][width - 1 - x] = pixel_temp;
       }
   }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
   //copy image
   RGBTRIPLE copy[height][width];
   for (int y = 0; y < height; y++)
   {
       for (int x = 0; x < width; x++)
       {
           copy[y][x] = image[y][x];
       }
   }

   for (int y = 0; y < height; y++)
   {
       for (int x = 0; x < width; x++)
       {
           //init RGB to 000
           image[y][x] = (RGBTRIPLE) {.rgbtBlue = 0, .rgbtGreen = 0, .rgbtRed = 0};
           for (int inner_y = -2; inner_y <= 2; inner_y++)
           {
               for (int inner_x = -2; inner_x <= 2; inner_x++)
               {
                   int source_x = x + inner_x;
                   int source_y = y + inner_y;
                   if (source_x < 0 || source_x > width || source_y < 0 || source_y > height)
                   {
                       continue;
                   }
                   image[y][x].rgbtBlue += copy[source_y][source_x].rgbtBlue / 25;
                   image[y][x].rgbtGreen += copy[source_y][source_x].rgbtGreen / 25;
                   image[y][x].rgbtRed += copy[source_y][source_x].rgbtRed / 25;
               }
           }
       }
   }
}
