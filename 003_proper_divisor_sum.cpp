#include <iostream>
using namespace std;

 int main(){
 	int n, i, prev, sum=1;
 	cin>>n;
 	prev = 1;
 	for (i=2; i<n; i++){
 		if(n%i == 0){
 			cout<<prev<<" + ";
 			prev = i;
 			sum = sum+i;
		 }
	 }
	 cout<<prev<<" = "<<sum;
	 return 0;
 }
