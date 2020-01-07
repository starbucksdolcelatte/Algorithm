#include <stdio.h>
#include <iostream>
using namespace std;

int digit_sum(int x){
	int a, i=0, sum=0;
	while(i<8){
		a = x%10;
		sum += a;
		x = (x-a)/10;
		i++;
	}
	return sum;
}

int main(){
	int n, i, idx, max = -1;
	
	//input
	//freopen("input.txt", "rt", stdin);
	scanf("%d", &n);
	int* sum = new int[n]();
	int* num = new int[n]();
	for(i=0; i<n; i++){
		scanf("%d", &num[i]);
		sum[i] = digit_sum(num[i]);
	}
	
	for(i=0; i<n; i++){
		if(max<sum[i]){
			max = sum[i];
			idx = i;
		}
	}
	printf("%d ", num[idx]);
	return 0;
}


