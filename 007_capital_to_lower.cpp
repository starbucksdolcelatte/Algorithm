#include <stdio.h>
using namespace std;

int main(){
	char s[100], res[100];
	int i, j=0;
	freopen("input.txt", "rt", stdin);
	gets(s); //scanf���� ����?
	/*
	scanf�� ���� �ձ����� �Է��� �޴´�. 
	%s, %d �� �Է� �޴� format ���� ���� 
	gets�� �� ���� �Է� �޴´�. 
	�׷��� ������ ������ ���� �ʱ� ������
	������ ������� ū ���� �Է��ϸ� ���� ��.
	fgets�� �� ������ �ذ��Ѵ�.
	fgets(���ۿ� ���� ������, sizeof(str), stdin)
	sizeof(int)����� �� ���� �ִ�. �ƹ�ư �Է¹��� ũ��	
	*/ 
	
	for(i=0; s[i]!='\0'; i++){
		if (s[i] !=' '){
			if(s[i]>=65 && s[i]<=90){ // if capital
				res[j++] = s[i]+32;   // make it lower
			}
			else res[j++] = s[i];
		}
	} 
	res[j] = '\0'; //++�����ڴ� ���߿� ����ǹǷ� �̹�++�� ���´�. 
	printf("%s\n", res);
}
