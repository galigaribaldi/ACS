import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Cliente01A
{
public static void main(String a[])
{
 Socket socket = null;
 String peticion = "Mensaje para el servidor";
 String respuesta = null;
 String nombre="";
 String bye="bye";
 int i=0;

while (true){
	 try
	 {
		if (i == 0){
	 		System.out.println("Me conecto al puerto 8000 del servidor");
	 		i = 1;
 		}
 	
		 socket = new Socket(a[0],8000);

		 Scanner teclado = new Scanner(System.in);
		 DataOutputStream dos = new DataOutputStream( socket.getOutputStream());
		 DataInputStream dis = new DataInputStream( socket.getInputStream() );
		 

	 	 peticion = teclado.nextLine();
	 	 dos.writeUTF(peticion);
 	 	//System.out.println("Le envio mi peticion: " + peticion);
		 dos.writeUTF(peticion);
		 respuesta = dis.readUTF();
		 System.out.println("Servidor: " + respuesta);

		 if(respuesta.equals(bye)) break;


		 dos.close();
		 dis.close();
		 socket.close();
	 }
	 catch(IOException e)
	 {
	 System.out.println("java.io.IOException generada");
	 e.printStackTrace();
	 }
}

}
}