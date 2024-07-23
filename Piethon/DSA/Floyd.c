int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}

/**
 * The Floyd's algorithm has the advantage of detecting cycles efficiently with a small memory overhead, making it  * a commonly used technique for cycle detection in linked lists.
 *
 * Remember that while this algorithm is efficient, the trade-off is that it won't give you the specific node where * the cycle starts. If you need to find the exact cycle starting point, you might need to use other methods like H * ashing or modifying the linked list structure.
 */
