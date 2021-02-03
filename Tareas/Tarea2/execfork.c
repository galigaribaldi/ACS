//Librerias necesarias para el funcionamiento del codigo
#include <stdio.h> 
#include <stdlib.h> 
#include <sys/types.h> 
#include <unistd.h>
// Se define una funcion hija, la cual recibe como argumentos, los parametros que se le den 
// en la consola
int spawn (char* program, char** arg_list) {
	//proceos
	pid_t child_pid;
	child_pid = fork ();
	// si el proceso no logra crear el proceso hijo creado, este simplemente retornara el pid
	if (child_pid != 0) 
		return child_pid;
	//En una segunda corrida con el proceso creado, se ejecuta como argumento la lista de argumentos
	//definida anterioremnte en el main, por lo que se ejecuta "ls -l /"
	else {
		execvp (program, arg_list);
		fprintf (stderr, "an error occurred in execvp\n"); 
		abort ();
	} 
}
/// Proceso Padre ejecuta "done With main Program"
int main () {
	char* arg_list[] = { "ls", "-l","/", NULL };
	spawn ("ls", arg_list);
	printf ("done with main program\n");
	return 0;
}