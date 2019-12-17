#include <stdio.h>
using namespace std;

int main(){
	char s[30];
	int stack=0, i;
	//freopen("input.txt", "rt", stdin);
	gets(s);
	
	for(i=0; s[i]!='\0'; i++){
		if(s[i]=='(') stack++;
		else if(s[i]==')'){
			if(stack > 0) stack--;
			else {
				printf("NO");
				return 0;
			}
		}
	}
	if(stack==0) printf("YES");
	else printf("NO");
	return 0;
}
