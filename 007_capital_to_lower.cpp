#include <stdio.h>
using namespace std;

int main(){
	char s[100], res[100];
	int i, j=0;
	freopen("input.txt", "rt", stdin);
	gets(s); //scanf와의 차이?
	/*
	scanf는 공백 앞까지만 입력을 받는다. 
	%s, %d 등 입력 받는 format 지정 가능 
	gets는 한 줄을 입력 받는다. 
	그러나 사이즈 제한을 두지 않기 때문에
	변수의 사이즈보다 큰 값을 입력하면 에러 남.
	fgets는 이 문제를 해결한다.
	fgets(버퍼에 대한 포인터, sizeof(str), stdin)
	sizeof(int)등등이 될 수도 있다. 아무튼 입력받을 크기	
	*/ 
	
	for(i=0; s[i]!='\0'; i++){
		if (s[i] !=' '){
			if(s[i]>=65 && s[i]<=90){ // if capital
				res[j++] = s[i]+32;   // make it lower
			}
			else res[j++] = s[i];
		}
	} 
	res[j] = '\0'; //++연산자는 나중에 수행되므로 이미++된 상태다. 
	printf("%s\n", res);
}
