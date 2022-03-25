#include<stdio.h>

//char flag[]="LaSERCTF{S0_C00L_W3Lc0M3_y0u_H4ck3r}\x00";
int c = 0;

void result(){
	char s[200];
	if(fgets(s,100,stdin)!=NULL){
		printf("HI\n");
		printf(s);
	}	
	if(c==0xaa)
		printf("\nLaSER_CTF{WH4t_h4pp3n3d?}\n");
	else
		printf("You loose\n");	

}


int main(){

	result();
	return 0;
}





