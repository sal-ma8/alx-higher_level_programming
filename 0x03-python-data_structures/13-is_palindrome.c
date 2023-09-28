#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function
 * @head: vp1
 * Return: jdbkjb
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *dooo = *head, *next, *prev = NULL;

	while (dooo)
	{
		next = dooo->next;
		dooo->next = prev;
		prev = dooo;
		dooo = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - function
 * @head: vp1
 * Return: rakm
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *hat, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	hat = reverse_listint(&tmp);
	mid = hat;

	tmp = *head;
	while (hat)
	{
		if (tmp->n != hat->n)
			return (0);
		tmp = tmp->next;
		hat = hat->next;
	}
	reverse_listint(&mid);

	return (1);
}
