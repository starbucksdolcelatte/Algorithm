#include <iostream>
using namespace std;

int main(){
 	int n, i, a, max = -214700000, min=2147000000;
 	cin>>n;
 	for (i=0; i<n; i++){
 		cin>>a;
 		if(a<min) min = a;
		if(a>max) max = a;
	 }
	 cout<<max-min;
	 return 0;
 }
