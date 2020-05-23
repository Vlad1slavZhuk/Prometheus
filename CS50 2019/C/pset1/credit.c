#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long n;
    do
    {
        n = get_long("Number: ");
    }
    while(n < 0);
    
    int sum1 = 0;
    int sum2 = 0;

    for (long l = n; l > 0; l /= 100)
    {
        sum1 += (l % 10);
    }
    
    for (long l = n / 10; l > 0; l /= 100)
    {
        if ((l % 10) * 2 > 9)
        {
            long a = ((l % 10) * 2) % 10;
            long b = ((l % 10) * 2) / 10;
            sum2 += a + b;
        }
        else
        {
            sum2 += (l % 10) * 2;
        }
    }
    int sum = sum1 + sum2;
    
    if (sum % 10 == 0)
    {
        if ((n >= 340000000000000L && n < 350000000000000L) || (n >= 370000000000000L && n < 380000000000000L))
         {
             printf("AMEX\n");
         }
         else if (n >= 5100000000000000L && n < 5600000000000000L)
         {
             printf("MASTERCARD\n");
         }
         else if ((n >= 4000000000000L && n < 5000000000000L) || (n >= 4000000000000000L && n < 5000000000000000L))
         {
             printf("VISA\n");
         }
         else
         {
             printf("INVALID\n");
         }
    }
    else 
    {
        printf("INVALID\n");
    }
}
