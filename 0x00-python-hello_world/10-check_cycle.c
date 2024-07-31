#include <stdio.h>
#include "lists.h"


/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the list
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	int *slow = list;
	int *fast = list;

	if (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		fast = fast->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
