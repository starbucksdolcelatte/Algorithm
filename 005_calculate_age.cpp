#include <stdio.h>
using namespace std;
int main(){
	char s[14];
	int i, age, year;
	//freopen("input.txt", "rt", stdin);
	scanf("%s", s);
	
	year = (s[0]-48)*10 + (s[1]-48);
	if(s[7]-48==1 || s[7]-48==2){
		age = 120 - year;
	}
	else{
		age = 20 - year;
	}
	printf("%d", age);
	if(s[7]=='1' || s[7]=='3') printf("%s", " M");
	if(s[7]=='2' || s[7]=='4') printf("%s", " W");

	return 0;
}
