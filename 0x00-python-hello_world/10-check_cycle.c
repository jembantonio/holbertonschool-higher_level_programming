#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list->next;

	if (list = NULL)
		return (0);

	while (slow != NULL && fast->next != NULL && fast != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
