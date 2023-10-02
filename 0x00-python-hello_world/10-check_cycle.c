#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - Checks if a singly linked list has a cycle.
* @list: A pointer to the head of the linked list.
*
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/
int check_cycle(listint_t *list)
{
if (list == NULL || list->next == NULL)
{
return (0);
}

listint_t *slow = list;
listint_t *fast = list;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
{
	return (1); // Cycle detected
}
}

return (0);
}

