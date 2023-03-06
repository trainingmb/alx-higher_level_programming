#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	if (current != NULL)
		temp = current->next;
	else
		return (0);

	while (current->next != NULL)
	{
		if (current == temp)
			return (1);
		temp = temp->next;
		if (temp == NULL)
		{
			current = current->next;
			temp = current->next;
		}
	}
	return (0);
}
