#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *temp;

	if (!head)
		return (NULL);

	/* allocate node */
	newnode = malloc(sizeof(listint_t));

	if (!newnode)
		return (NULL);
	/* put data into new node */
	newnode->n = number;

	/* traverse the list */
	if (*head)
	{
		/* setting temporary pointer to start of list */
		temp = *head;

		/* inserting the node at the beginning of the list */
		if (number <= temp->n)
		{
			newnode->next = temp;
			*head = newnode;
		}

		else
		{
			/* if number is greater than the next n of the linked list */
			while (number > (temp->next)->n)
    				/* set the pointer temp to point to the next node */
				temp = temp->next;
		}
		/* move pointers ahead */
		newnode->next = temp->next;
		temp->next = newnode;
	}

	/* insert new node into empty list */
	else
	{
		newnode->next = NULL;
		*head = newnode;
	}

	return (newnode);
}
