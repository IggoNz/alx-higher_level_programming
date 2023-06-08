#include "lists.h"
/**
 * check_cycle: checks a linked list to see if it has a cycle
 * @list: the list of interest being checked
 * Return: if the linked list has a cyle return 1, else return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
