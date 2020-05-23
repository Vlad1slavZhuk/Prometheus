#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void shifr(string text, int key);
bool check(string text);

int main(int argc, string argv[])
{
    if (argc == 2 && check(argv[1]))
    {
        int key = atoi(argv[1]);
        string text = get_string("plaintext:  ");
        shifr(text, key);
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    return 0;
}

bool check(string text)
{
    for (int i = 0; i < strlen(text); i++)
    {
        if(!isdigit(text[i]))
        {
            return false;
        }
    }
    return true;
}

void shifr(string text, int key)
{
    printf("ciphertext: ");
        for (int i = 0; i < strlen(text); i++)
        {
            if (isalpha(text[i]))
            {
                if (islower(text[i]))
                {
                    char a = (((text[i] - 'a') + key) % 26) + 'a';
                    printf("%c", a);
                }
                else
                {
                    char a = (((text[i] - 'A') + key) % 26) + 'A';
                    printf("%c", a);
                }
            }
            else
            {
                printf("%c", text[i]);
            }
        }
        printf("\n");
}
