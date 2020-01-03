#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
	int n, i, j, idx;
	
	//input
	//freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	int* arr = new int[n+1]();
	
	for(i=1; i<n+1; i++){
		j=i;
		while(j<n+1){
			arr[j]++;
			j += i;
		}
		/*
		for(j=1; j<n+1; j++){
			printf("%d ", arr[j]);
		}
		printf("\n");
		*/
	}
	for(i=1; i<n+1; i++){
		printf("%d ", arr[i]);
	}
	return 0;
}
