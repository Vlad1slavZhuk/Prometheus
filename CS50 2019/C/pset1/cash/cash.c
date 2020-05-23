#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int coins;
    do
    {
        float f = get_float("Change: ");
        coins = round(f * 100);
    }
    while(coins <= 0);
    
    int quarters = coins / 25;
    int dimes = (coins % 25) / 10;
    int nickels = ((coins % 25) % 10) / 5;
    int pennies = ((coins % 25) % 10) % 5;

    int count = quarters + dimes + nickels + pennies;

    printf("%d\n", count);
}