#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * list_len - get length f=of singly linked list
 * @h: the head of the list
 * Return: the length of the list
 */
int list_length(const listint_t *h)
{
    int s;
    const listint_t *iter;

    iter = h;
    for (s = 0; iter != ((void *) 0); iter = iter->next)
    {
        s++;
    }
    return (s);
}
/**
 * move_forward - A function to get the int value at [steps]
 * away from [current]
 * @current: where to start counting
 * @steps: number of steps
 * Return: the int value of the list indexed
 */
int move_forward(listint_t *current,int steps)
{
    listint_t *temp;

    temp = current;
    while(steps > 0)
    {
        temp = temp->next;
        steps--;
    }
    return (temp->n);
}

/**
 * is_palindrome - Checks if the head list is palindrome
 * @head: The start of the list
 *
 * Return: if is palindrome
 */
int is_palindrome(listint_t **head)
{
    int len, left, right, pal;
    listint_t *temp;
    pal = 1;
    if (head == NULL || *head == NULL)
        return (1);
    len = list_length(*head);
    left = 0;
    right = len - 1;
    temp = *head;
    while ((pal) && (left < right))
    {
        if(temp->n != move_forward(temp, right))
        {
            pal = 0;
            break;
        }
        left++;
        right = right - 2;
        temp = temp->next;
    }
    return (pal);
}