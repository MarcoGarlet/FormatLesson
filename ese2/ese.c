#include<stdio.h>

int main(){
	int i;
	char s1[50];
	char s[200];	
	for (i = 0;i<2;i++){
		printf("Who are you?\n");
		fgets(s,200,stdin);
		printf("Thank u!\n");
		printf(s);
	}
	printf("Give me some bytes, be kind!\n");
	gets(s1);	
	printf("Thank u\n");	
		
	

	return 0;
}
