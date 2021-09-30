#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
	int			x;
	char		*str;
	struct Node *next;
} Node;

// Find in linked list
Node *find_in_linked(Node root, char *str)
{
	Node *curr;

	curr = &root;
	while (curr != NULL)
	{
		if (strcmp(curr->str, str))
			return (curr);
		curr = curr->next;
	}
	return (NULL);
}

void	remove_linked_node(Node **root, int value)
{
	Node	*curr;
	Node	*save;

	curr = *root;
	if ((*root)->x == value)
	{
		(*root) = (*root)->next;
		return ;
	}
	while (curr->next != NULL)
	{
		if (value == curr->x)
			save->next = curr->next;
		save = curr;
		curr = curr->next;
	}
}

void	insert_end(Node **root, int value)
{
	Node	*new_node;
	Node	*curr;

	new_node = malloc(sizeof(Node));
	if (!new_node)
		exit(1);
	new_node->next = NULL;
	new_node->x = value;
	curr = *root;
	while (curr->next != NULL)
		curr = curr->next;
	curr->next = new_node;
}

void	insert_beg(Node **root, int value)
{
	Node	*new_node;
	Node	*save;

	printf("Teste\n");
	new_node = malloc(sizeof(Node));
	if (!new_node)
		exit(1);
	new_node->x = value;
	save = *root;
	*root = new_node;
	(*root)->next = save;
}

int main(void)
{
	Node node, elem2;
	// Not a good way to use linked list
	node.x = 15;
	node.next = &elem2;
	elem2.x = -2;
	elem2.next = NULL;
	
	// With mem allocation (good_way)

	Node root;

	root.x = 15;
	root.next = malloc(sizeof(Node));
	root.next->x = -2;
	root.next->next = NULL;
	// Iterate over a loop
	Node *curr = &root;

	while (curr != NULL)
	{
		printf("%d\n", curr->x);
		curr = curr->next;
	}
	free (root.next);

	// Best way!!
	Node *proot = malloc(sizeof(Node));
	if (!proot)
		exit(2);
	proot->x = 15;
	proot->next = NULL;
	
	insert_end(&proot, 20);
	insert_end(&proot, 30);
	insert_end(&proot, 40);
	remove_linked_node(&proot, 15);
	insert_beg(&proot, 10);
	remove_linked_node(&proot, 10);
	curr = proot;
	while (curr != NULL)
	{
		printf("value %d\n", curr->x);
		curr = curr->next;
	}

	return (0);
}