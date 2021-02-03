import java.net.*;
import java.io.*;
import java.util.Scanner;

public class Servidor01A{
	public static void main(String a[]){
		ServerSocket serverSocket = null;
		Socket socket = null;
		String peticion = null;
		String respuesta = null;
		String bye="bye";
		try{
			System.out.println("Escuchando por el puerto: "+a[0]);
			Integer x = Integer.valueOf(a[0]);
			serverSocket = new ServerSocket(x);
		}catch(IOException e){
			System.out.println("java.io.IOException generada");
			e.printStackTrace();
		}
		System.out.println("Esperando a que los clientes se conecten...");
		while(true){
			try{
				socket = serverSocket.accept();
				System.out.println("Se conecto un cliente: " + socket.getInetAddress().getHostName());
				Scanner teclado = new Scanner(System.in);
				String nombre="";
				DataInputStream dis = new DataInputStream( socket.getInputStream() );
				DataOutputStream dos = new DataOutputStream( socket.getOutputStream());
				peticion = dis.readUTF();
				System.out.println("El cliente dice: " + peticion);
				nombre = teclado.nextLine();
				dos.writeUTF(nombre);
				if(peticion.equals(bye)){
					break;
				}	
				dos.close();
				dis.close();
				socket.close();
				socket = null;
			}catch(IOException e){
				System.out.println("java.io.IOException generada");
				e.printStackTrace();
			}
		}
	}
}
