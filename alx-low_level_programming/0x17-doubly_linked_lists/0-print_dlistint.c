#include "lists.h"
/**
 * print_dlistint - func11
 * @h: vp1
 * Return:qwq
 */
size_t print_dlistint(const dlistint_t *h)
{
	int ha;

	ha = 0;

	if (h == NULL)
		return (ha);

	while (h->prev != NULL)
		h = h->prev;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		ha++;
		h = h->next;
	}

	return (ha);
}
