#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
	int n, i, j, idx, tmp, rank=1;
	int* arr = new int[n];
	
	//input
	freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	for(i=0; i<n; i++){
		scanf("%d", &arr[i]);
	}
	
	for(i=0; i<n-1; i++){
		idx = i;
		for(j=i+1; j<n; j++){
			if(arr[j]>arr[idx])	idx = j;
		}
		tmp = arr[i];
		arr[i] = arr[idx];
		arr[idx] = tmp;
	}
	for(i=1; i<n; i++){
		if(arr[i-1]!=arr[i]) rank++;
		if(rank==3) break;
	}
	printf("%d", arr[i]);
	return 0;
}
