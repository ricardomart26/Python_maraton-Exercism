#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
	int	x;
	struct Node *next;
} Node;


int main(int ac, char *av)
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
	free (root.next);
	return (0);
}