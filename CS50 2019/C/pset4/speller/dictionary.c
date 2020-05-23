// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];
int totalWords = 0;

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // TODO
        node *currNode = malloc(sizeof(node));
        if (!currNode)
        {
            unload();
            return false;
        }
        
        strcpy(currNode->word, word);
        currNode->next = NULL;
        
        int index = hash(currNode->word);
        if (hashtable[index] != NULL)
        {
            currNode->next = hashtable[index];
        }
        hashtable[index] = currNode;
        totalWords++;
    }

    // Close dictionary
    fclose(file);

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return totalWords;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    node *cursor = hashtable[hash(word)];

    if (strcasecmp(cursor->word, word) == 0)
    {
        return true;
    }

    while (cursor->next != NULL)
    {
        cursor = cursor->next;
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
    }

    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    node *tmp;
    node *cursor;

    // repeats for every index in the table
    for (int i = 0; i < N; i++)
    {
        if (hashtable[i] == NULL)
        {
            continue;
        }

        cursor = hashtable[i];
        tmp = cursor;

        // until the end of the list keeps freeing the memory allocated in load
        while (cursor->next != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
        free(cursor);
    }
    return true;
}
