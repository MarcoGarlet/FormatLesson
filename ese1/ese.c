#include<stdio.h>
#include <stdlib.h>
#include<time.h>

int main(){
	srand(time(0));
	char s[800];
	unsigned long long random_number = rand()%(1ULL<<64-1); // random number from 0 to max 64 bit representation
	unsigned long long guess;
	printf("Tell me who are you: \n");
	if(fgets(s,800,stdin)!=NULL){
		//fflush(stdout);
		puts("Hi ");
		printf(s);
		puts("\nTell me my secret: ");
		scanf("%llu",&guess);
		printf("\nGuess = %llu\n",guess);
		if(guess == random_number){
			printf("\nl4s3rCTF{%llu th3 numb3r 0f th3 b345t!!!}\n",guess);
		}
		else{
			printf("\nThe number was %llu\nBye!\n",random_number);
		}
	}
	return 0;
}
