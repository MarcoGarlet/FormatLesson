#include<stdio.h>
#include <stdlib.h>

int c=0;
int main(){
	char s[100];
	gets(s);
	int *pc=&c;
	printf("\nc@%p\n",pc);
	printf(s);
	if(c==0){
		printf("\nBye!\n");
	}
	else{
		printf("\nl4s3rCTF{wr1t3_w1th_f0rm4t_i5_500_c00l!}\n");
	}


}








