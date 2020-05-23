#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void shifr(string text, string key);
bool check(string text);

int main(int argc, string argv[])
{
    if (argc == 2 && check(argv[1]))
    {
        string key = argv[1];
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
        if(!isalpha(text[i]))
        {
            return false;
        }
    }
    return true;
}

void shifr(string text, string key)
{
    printf("ciphertext: ");
    int kLen = strlen(key);
        for (int i = 0, j = 0, n = strlen(text); i < n; i++)
        {
            int ch = tolower(key[j % kLen]) - 'a'; 
            if (isupper(text[i]))
            {
                char a = 'A' + ((text[i] - 'A' + ch) % 26);
                printf("%c", a);
                j++;
            }
            else if (islower(text[i]))
            {
                char a = 'a' + ((text[i] - 'a' + ch) % 26);
                printf("%c", a);
                j++;
            }
            else
            {
                printf("%c", text[i]);
            }
        }
        printf("\n");
}
