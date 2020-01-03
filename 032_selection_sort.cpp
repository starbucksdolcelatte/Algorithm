#include <stdio.h>
#include <iostream>
using namespace std;

// Selection Sort
int main(){
	int n, i, j, idx, tmp;
	freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	int* arr = new int[n];
	for(i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	
	for(i=0; i<n; i++){
		idx = i;
		printf("%d\n", i);
		for(j=i+1; j<n; j++){
			printf("%d ", j);
			if(arr[idx] > arr[j]) {
				idx = j;
			}
		}
		printf("\n");
		tmp = arr[i];
		arr[i] = arr[idx];
		arr[idx] = tmp;
		
		for(j=0; j<n; j++){
			printf("%d ", arr[j]);
		}
		printf("\n\n");
	}
	return 0;
}
