#include <stdio.h>
using namespace std;

int main(){
	//freopen("input.txt", "rt", stdin);
	char s[50];
	int cnt=0, res=0, i;
	scanf("%s", s);
	
	// 1. Get the numbers
	for(i=0; s[i]!='\0'; i++){
		if(s[i]>=48 && s[i]<= 57) res = res*10 + (s[i]-48);
	}
	printf("%d\n", res);
	
	// 2. Find factor
	for(i=1; i<=res; i++){
		if(res%i==0) cnt++;
	}
	printf("%d", cnt);
	
	return 0;
 }
