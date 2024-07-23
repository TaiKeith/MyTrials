#include "lists.h"

/**
 * is_palindrome - A function that checks if a linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 1 if it's a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	/*Move slow to the middle, and reverse the second half*/
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		/*Store the original next pointer*/
		temp = slow->next;
		/*Reverse the direction of the next pointer*/
		slow->next = prev;
		/*Update the prev pointer to the current node*/
		prev = slow;
		/*Move to the next node in the original list*/
		slow = temp;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
