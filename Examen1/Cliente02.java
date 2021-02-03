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