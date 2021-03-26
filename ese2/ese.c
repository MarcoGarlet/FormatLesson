#include<stdio.h>

int main(){
	char s1[50];
	char s[200];	
	printf("Who are you?\n");
	if (fgets(s,200,stdin)!=NULL){
		printf("Thank u!\n");
		printf(s);
		printf("Give me some bytes, be kind!\n");
		gets(s1);	
		printf("Thank u\n");	
	}
		
	

	return 0;
}
