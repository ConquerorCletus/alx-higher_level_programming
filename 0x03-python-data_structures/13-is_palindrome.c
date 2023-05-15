#include "lists.h"

/**
 * reverse_listint - reverses linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head pointer
 * Return: 1 for palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp1 = *head, *tmp2 = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		tmp2 = tmp2->next->next;
		if (!tmp2)
		{
			dup = tmp1->next;
			break;
		}
		if (!tmp2->next)
		{
			dup = tmp1->next->next;
			break;
		}
		tmp1 = tmp1->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
