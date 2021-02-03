# Examen 1

**Nombre del Alumno 1: **Cabrera Garibaldi Hernán Galileo

**Nombre del Alumno 2: **Maceda Nazario Luis Martín

**Nombre del profesor:** Carlos Alberto Román Zamitis

**Clave de la Materia: **2946

**Nombre de la Materia:** Arquitectura Cliente Servidor

**Semestre: ** 2021-1

## Servidor

En este tramo se describe el código variante para el servidor, se optó por hacer una versión del código visto en clase

```java
import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Servidor02{
	public static void main(String a[]){
		ServerSocket serverSocket = null;
		Scanner sc = new Scanner(System.in);
		Socket socket = null;
		String peticion = "";
		String respuesta = "";
		String salir = "salir";
		String ls = "ls -l";
		String variable = "";
		String line = "";
		int i = 0;
		//System.out.println(a[0]);
		try{
			System.out.println("Escuchando por el puerto: "+a[0]);
			Integer x = Integer.valueOf(a[0]);
			serverSocket = new ServerSocket(x);
		}
		catch(IOException e){
			System.out.println("java.io.IOException generada");
			e.printStackTrace();
		}
		System.out.println("Esperando a que los clientes se conecten...");
		while(true){
			try{
				socket = serverSocket.accept();
				if (i == 0){
					System.out.println("Se conecto un cliente: " + socket.getInetAddress().getHostName());
					}
				i = 1;
				DataInputStream entrada = new DataInputStream( socket.getInputStream());
				peticion = entrada.readUTF();
				System.out.println("El mensaje que me envio el cliente es: " + peticion);
				if(peticion.equals(salir)){
					break;
				}
				if(peticion.equals(ls)){
					String[] cmd = {"/bin/bash","-c","ls -l"};
        			Process pb = Runtime.getRuntime().exec(cmd);
        			BufferedReader input = new BufferedReader(new InputStreamReader(pb.getInputStream()));
        			while ((line = input.readLine()) != null) {
            			//System.out.println(line);
						variable =variable + line+ "\n";
        			}
				}
				DataOutputStream salida = new DataOutputStream( socket.getOutputStream());
				if (peticion.equals(ls)){
					salida.writeUTF(variable);
					System.out.println("Enviando Respuesta del ls -l");
					entrada.close();
					salida.close();
					socket = null;
				}else{
					System.out.println("Escribe Mensaje al cliente:");
					String mensaje = sc.nextLine();
					salida.writeUTF(mensaje);
					System.out.println("El mensaje que le envio al cliente es: " + mensaje);
					entrada.close();
					salida.close();
					socket = null;
				}
 			}catch(IOException e){
				 System.out.println("java.io.IOException generada");
				 e.printStackTrace();
				 }
 		}
	}
}
```

![](Capturas/Captura de Pantalla 2020-12-09 a la(s) 22.36.25.png)

## Cliente 

En este tramo se muestra el código correspondiente al cliente

```c
import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Cliente02{
	public static void main(String a[]){
		Socket socket = null;
		Scanner sc = new Scanner(System.in);
 		String peticion ="";
 		String respuesta = "";
 		String salir="salir";
 		int i=0;
  		while(true){
			try{
				Integer x = Integer.valueOf(a[1]);				
 				socket = new Socket(a[0],x);
 				DataOutputStream dos = new DataOutputStream( socket.getOutputStream());
 				DataInputStream dis = new DataInputStream( socket.getInputStream() );
				if (i == 0){
					System.out.println("Me conecto al puerto: "+ a[1]);
				}
				i = 1;
				System.out.println("Escribe el mensaje para el servidor:");
				peticion = sc.nextLine();
				dos.writeUTF(peticion);
				if (peticion.equals(salir)){
					break;
				}
				else{
					System.out.println("El mensaje enviado: " + peticion);
					respuesta = dis.readUTF();
					System.out.println("El mensaje que me envio el servidor es: " + respuesta);
					dos.close();
					dis.close();
					socket.close();
				}
 			}
 			catch(IOException e){
 				System.out.println("java.io.IOException generada");
 				e.printStackTrace();
 			}
  		}
 
	}
}
```

![](Capturas/Captura de Pantalla 2020-12-09 a la(s) 22.37.05.png)

## Ejecutando comando ls -l

En esta parte se ejecuta el comando ls -l desde el programa de Java

![Captura de Pantalla 2020-12-09 a la(s) 22.38.51](Capturas/Captura de Pantalla 2020-12-09 a la(s) 22.38.51.png)