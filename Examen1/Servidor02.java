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