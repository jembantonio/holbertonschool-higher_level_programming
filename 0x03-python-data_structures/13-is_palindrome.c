#include "lists.h"

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: a pointer to the linked listint_t
 *
 * Return: 0 if not a palindrome or 1 if it is palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len, *arr, i, j;

	temp = *head;
	len = 0;

	while (temp != NULL)
	{
		temp = temp->next;
		len++;
	}

	arr = malloc(sizeof(int) * len);

	temp = *head;
	i = 0;

	while (temp != NULL)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}

	for (i = 0, j = len - 1; i < j; i++, j--)
		if (arr[i] != arr[j])
			return (0);

	return (1);
}
