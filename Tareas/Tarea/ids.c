#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
int main(void){
	printf("REal user ID: %d\n", getuid());
	printf("Effective User ID: %d\n",getuid());
	printf("Real group ID: %d\n", getgid());
	printf("Effective group ID: %d\n", getgid());
	return 0;
}
