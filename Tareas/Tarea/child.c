#include <stdio.h>
#include <stdlib.h>
#include<unistd.h>
int main(void) { //Tipo de dato que identifica el proceso del Hijo
	pid_t child;
	if((child = fork()) == -1) {
		//fork() Devuelve valores entero
		//Cero: Se ha creado el proceso Hijo
		//Valor positivo: Se devuelve al proceso padre a quien lo mande a llamar
		//Valor engativo: Fallo la creación del proceso Hijo
		perror("fork"); //Mensaje de error
		exit(EXIT_FAILURE); //Finaliza la llamada del rpoceso
	}
	else if(child == 0) { //Cuando chil es igual a o significa que el proceso ha concluido
		puts("in child");
		printf("\tchild pid = %d\n", getpid());//Id del proceso
		printf("\tchild ppid = %d\n", getppid());//ID del proceso
		exit(EXIT_SUCCESS);//Finaliza la ejecucion exitosa
	} else {
		puts("in parent");
		printf("\tparent pid = %d\n",
		getpid());
		printf("\tparent ppid = %d\n", getppid());
	}
	exit(EXIT_SUCCESS);//Finaliza la ejecucion
}
