import java.io.*;
import java.util.Scanner;

public class pruebas{
    public static void main(String[] args) throws IOException {

        String[] cmd = {"/bin/bash","-c","ls -l"};
        Process pb = Runtime.getRuntime().exec(cmd);

        String line;
        BufferedReader input = new BufferedReader(new InputStreamReader(pb.getInputStream()));
        while ((line = input.readLine()) != null) {
            System.out.println(line);
        }
        input.close();
    }
}