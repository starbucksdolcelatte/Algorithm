#include <stdio.h>
#include <stdlib.h>
#define TRUE 1
#define FALSE 0

typedef struct _Node {
	int data;
	struct _Node *next;
}Node;

typedef struct _LinkedList {
	int numOfItems;
	Node *head;
	Node *tail;
	Node *cur;
}LinkedList;

void ListInit(LinkedList *plist) {
	plist->head = NULL;
	plist->tail = NULL;
	plist->numOfItems = 0;
}

int IsEmpty(LinkedList* plist) {
	if (plist->numOfItems == 0) {
		return TRUE;
	}
	else {
		return FALSE;
	}
}

void InsertItem(LinkedList* plist, int data) {
	Node * newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	if (plist->head == NULL) {
		plist->head = newNode;
		plist->tail = newNode;
	}
	else {
		plist->tail->next = newNode;
		plist->tail = plist->tail->next;
	}
	newNode->next = plist->head; //circular
	(plist->numOfItems)++;
	plist->cur = plist->head;
} // end of InsertItem()

int RemoveItem(LinkedList* plist, int k) {
	Node* delNode;
	Node* prev;
	int i, ret;
	if (IsEmpty(plist))
		return -1;
	else {
		delNode = plist->cur;
		prev = plist->cur;
	}
	for (i = 0; i < k-1; i++) {
		prev = delNode;
		delNode = delNode->next;
	}
	prev->next = delNode->next;
	plist->cur = delNode->next;
	ret = delNode->data;
	free(delNode);
	(plist->numOfItems)--;
	return ret;
}

int main() {
	int n, k, i, ret;
	LinkedList list;
	ListInit(&list);
	scanf("%d %d", &n, &k);

	for (i = 1; i <= n; i++) {
		InsertItem(&list, i);
	}
	printf("<");
	while (!IsEmpty(&list)) {
		ret = RemoveItem(&list, k);
		printf("%d", ret);
		if (IsEmpty(&list)) printf(">");
		else printf(", ");
	}
	return 0;
}