#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head of linked list
 * @number: number
 * Return: the address of the new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *prev_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == false)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == false)
	{
		*head = new_node;
		return (new_node);
	}

	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;
	while (current_node && number > current_node->n)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	new_node->next = current_node;
	prev_node->next = new_node;

	return (new_node);
}
