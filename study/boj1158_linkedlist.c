/*
https://www.acmicpc.net/problem/1158
## 문제
조세퍼스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 
양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 
이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
원에서 사람들이 제거되는 순서를 (N, K)-조세퍼스 순열이라고 한다. 
예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

## 입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. 
(1 ≤ K ≤ N ≤ 5,000)
예제 입력
7 3

## 출력
예제와 같이 조세퍼스 순열을 출력한다.
예제 출력
<3, 6, 2, 7, 5, 1, 4>
*/
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